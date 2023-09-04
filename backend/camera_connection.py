"""
########################################
---------------------------------------

Made with Malek & Milad

Features:

    ● Create Unlimite Object of Cameras and Live Preview By serial number
    ● Set Bandwitdh Of each Cameras
    ● Set gain,exposure,width,height,offet_x,offset_y
    ● Get tempreture of Cmeras
    ● Set Trigger Mode on
    ● There are Some diffrents between ace2(pro) and ace

---------------------------------------
########################################
"""

from pickle import FALSE
from pypylon import pylon
import cv2
import time
import numpy as np
import sqlite3
import threading
from pypylon import genicam

from PySide6.QtCore import QDateTime as sQDateTime
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import QThread as sQThread
from PySide6.QtCore import Signal




DEBUG = True



# import database_utils

show_eror = False

class Collector(sQObject):
    trig_signal = Signal()
    finished = Signal()
    def __init__(self, serial_number,gain = 0 , exposure = 70000, max_buffer = 20, trigger=True, delay_packet=100, packet_size=1500 ,
                frame_transmission_delay=0 ,width=1000,height=1000,offet_x=0,offset_y=0, manual=True, list_devices_mode=False, trigger_source='Line1',parent=None):
        """Initializes the Collector
        Args:
            gain (int, optional): The gain of images. Defaults to 0.
            exposure (float, optional): The exposure of the images. Defaults to 3000.
            max_buffer (int, optional): Image buffer for cameras. Defaults to 5.
        """
        super(Collector,self).__init__(parent)
        self.gain = gain
        self.exposure = exposure
        self.max_buffer = max_buffer
        self.cont_eror=0
        self.serial_number = serial_number
        self.trigger = trigger
        self.trigger_source = trigger_source
        self.dp = delay_packet
        self.ps=packet_size
        self.ftd=frame_transmission_delay
        self.width=width
        self.height=height
        self.offset_x=offet_x
        self.offset_y=offset_y
        self.manual=manual
        self.list_devices_mode=list_devices_mode
        self.exitCode=0
        self.camera = None
        self.capturing = True
        # if show_eror:
        #     self.window_eror = UI_eror_window()

        self.__tl_factory = pylon.TlFactory.GetInstance()
        devices = []
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_Mono8
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

        for device in self.__tl_factory.EnumerateDevices():              
                devices.append(device)


        for device in devices:
            camera = pylon.InstantCamera(self.__tl_factory.CreateDevice(device))
            if camera.GetDeviceInfo().GetSerialNumber() == str(self.serial_number):                
                self.camera = camera
                break
        try:
            if self.camera!=None:
                if self.camera.GetDeviceInfo().GetDeviceClass() == 'BaslerGigE':
                    self.camera.Open()
                    self.camera.GevSCPSPacketSize.SetValue(self.ps)
                    self.camera.GevSCPD.SetValue(self.dp)
                    self.camera.GevSCFTD.SetValue(self.ftd)
                    self.camera.GevSCBWR.SetValue(10)
                    self.camera.GevSCBWRA.SetValue(3)
                    self.camera.Close()
        except:
            if self.camera !=None:
                self.camera.Close()
            print('Eror in set bandwisth')
        # assert len(devices) > 0 , 'No Camera is Connected!'
        
    def set_capturing(self,status):
        self.capturing = status

    def tempreture(self):
        device_info = self.camera.GetDeviceInfo()
        model=str(device_info.GetModelName())
        model=model[-3:]
        return self.camera.TemperatureAbs.GetValue()


    def start_grabbing(self):
        if self.camera:
            device_info = self.camera.GetDeviceInfo()
            model=str(device_info.GetModelName())


            self.camera.Open()

            if self.manual:

                    try:
                        self.camera.GainRaw.SetValue(self.gain)
                    except:
                        #  self.camera.GainRaw.SetValue(192)
                        print(f'{self.serial_number} GainRaw set Error')

                    try:
                        self.camera.StopGrabbing()
                        self.camera.ExposureTimeRaw.SetValue(self.exposure)
                    except:
                        # self.camera.ExposureTimeRaw.SetValue(1000)
                        print(f'{self.serial_number} ExposureTimeRaw set Error')

                    try:
                        # self.camera.Close()
                        self.camera.StopGrabbing()
                        self.camera.Width.SetValue(self.width)
                    except:
                        print(f'{self.serial_number} Width set Error')
                    try:
                        # self.camera.Close()
                        # self.camera.StopGrabbing()
                        self.camera.Height.SetValue(self.height)
                    except:
                        print('height errror')
                        # print(f'{self.serial_number} Height set Error')
                    try:
                        self.camera.Open()
                        self.camera.OffsetX.SetValue(self.offset_x)
                    except:
                        print(f'{self.serial_number} OffsetX set Error')
                    try:
                        self.camera.Open()
                        self.camera.OffsetY.SetValue(self.offset_y)
                    except:
                        print(f'{self.serial_number} OffsetY set Error')
                    


            self.camera.Close()

            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 

            self.camera.Open()

            if self.trigger=='On':
                self.camera.TriggerMode.SetValue('On')
                #self.camera.TriggerSource.SetValue(self.trigger_source)
                print('triggeron on %s' % self.trigger_source)
            else:
                self.camera.TriggerMode.SetValue('Off')
                print('triggeroff')

            self.exitCode=0

            return True, 'start grabbing ok'
            
    
    def stop_grabbing(self):
        if self.camera:
            self.camera.Close()


    def off_trigger(self):
        self.camera.TriggerMode.SetValue('Off')
    
    def on_trigger(self):

        self.camera.TriggerMode.SetValue('On')
            
        
    def listDevices(self):
        """Lists the available devices
        """
        for i ,  camera in enumerate(self.cameras):
            device_info = camera.GetDeviceInfo()


    def serialnumber(self):
        serial_list=[]
        try:
            if self.camera !=None:
                for i ,  camera in enumerate(self.cameras):
                    device_info = camera.GetDeviceInfo()
                    serial_list.append(device_info.GetSerialNumber())
        except:
            print('Error in serial number camera connection')
            pass
        return serial_list         



    def getPictures(self, time_out = 50):
        
        if self.camera:
            Flag=False
            try:
                if self.camera.IsGrabbing():

                    grabResult = self.camera.RetrieveResult(time_out, pylon.TimeoutHandling_ThrowException)
                    if grabResult.GrabSucceeded():
                        image = self.converter.Convert(grabResult)

                        img = image.GetArray()
                        Flag =  True
                    else:
                        img=np.zeros([1200,1920,3],dtype=np.uint8)
                        self.cont_eror+=1
                        print('eror',self.cont_eror)
                        print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
                        Flag=False

                else:
                        # print('erpr')
                        img=np.zeros([1200,1920,3],dtype=np.uint8)
                        Flag=False

            except:

                img=np.zeros([1200,1920,3],dtype=np.uint8)
                Flag=False
            # self.image = img
            if Flag:
                return True, img
            else:

                return False, np.zeros([1200,1920,3],dtype=np.uint8)



        return False, np.zeros([1200,1920,3],dtype=np.uint8)

    def software_trig(self):

        self.camera.TriggerSoftware.Execute()


    def get_picture_while(self):

        while True:
            if self.capturing:
                cv2.waitKey(100)
                ret, self.image = self.getPictures()

                if DEBUG:
                    ret,self.image = True,(np.random.rand(500,500,3)*255).astype('uint8')

                if ret:
                    self.trig_signal.emit()
            else:
                break
        self.finished.emit()

    def update_parms(self, parms):
        for parm, value in parms.items():
            if parm == 'gain_value':
                try:
                    self.gain = int(value)
                    self.camera.GainRaw.SetValue(self.gain)
                except:
                    pass


            elif parm == 'expo_value':
                try:
                    self.exposure = int(value)
                    self.camera.ExposureTimeRaw.SetValue(self.exposure)
                except:
                    pass

            
            elif parm == 'width':
                try:
                    self.width = int(value)
                    self.camera.Width.SetValue(self.width)
                except:
                    pass


            elif parm == 'height':
                try:
                    self.height = int(value)
                    self.camera.Height.SetValue(self.height)
                except:
                    pass
            

            elif parm == 'offsetx_value':
                try:
                    self.offset_x = int(value)
                    self.camera.OffsetX.SetValue(self.offset_x)
                except:
                    pass
            
            elif parm == 'offsety_value':
                try:
                    self.offset_y = int(value)
                    self.camera.OffsetY.SetValue(self.offset_y)
                except:
                    pass
            

            elif parm == 'trigger_mode':
                try:
                    self.trigger = str(value)
                    self.camera.TriggerMode.SetValue(self.trigger)
                except:
                    pass

            elif parm == 'packet_size':
                try:
                    self.packet_size = str(value)
                    self.camera.packetsize_spinbox.SetValue(self.packet_size)
                except:
                    pass

            elif parm == 'transmission_delay':
                try:
                    self.transmission_delay = str(value)
                    self.camera.transmissiondelay_spinbox.SetValue(self.transmission_delay)
                except:
                    pass

            elif parm == 'interpacket_delay':
                try:
                    self.interpacket_delay = str(value)
                    self.camera.packetdelay_spinbox.SetValue(self.interpacket_delay)
                except:
                    pass


if __name__ == "__main__":


    collector = Collector(
        "20306145",
        exposure=3000,
        gain=10,
        trigger='On',
        delay_packet=81062,
        packet_size=9000,
        frame_transmission_delay=18036,
        height=500,
        width=500,
        offet_x=16,
        offset_y=4,
        manual=True
    )

    # # x=collector.get_cam()

    collector.start_grabbing()
    # # collector.start_grabbing()
    # cameras = collector

    # cameras.start_grabbing()
    # cameras.getPictures()
    # # print(cameras.)

    while True:

        #     # for cam in cameras:
        #     #         cam.trigg_exec()

        #     # for cam in cameras:
        #     #print(cam.camera.GetQueuedBufferCount())
        img = collector.getPictures()
        # print(img)
        img=img[1]
        # print(img.shape)
        # print(cam.camera.GetQueuedBufferCount())
        cv2.imshow("img1", cv2.resize(img, None, fx=0.5, fy=0.5))
        img=np.uint8(img)
        # cv2.imshow('img',img)
        cv2.waitKey(50)
    #     # img = cameras[1].getPictures()
    #     # #print(cam.camera.GetQueuedBufferCount())
    #     # cv2.imshow('img2', cv2.resize( img, None, fx=0.5, fy=0.5 ))
    #     # cv2.waitKey(50)
    #     # img = cameras[2].getPictures()
    #     # #print(cam.camera.GetQueuedBufferCount())
    #     # cv2.imshow('img3', cv2.resize( img, None, fx=0.5, fy=0.5 ))
    #     # cv2.waitKey(50)
    #     # img = cameras[3].getPictures()
    #     # #print(cam.camera.GetQueuedBufferCount())
    #     # cv2.imshow('img4', cv2.resize( img, None, fx=0.5, fy=0.5 ))
    #     # cv2.waitKey(50)

    #     # time.sleep(0.330)
    #     # while cam.camera.GetQueuedBufferCount()!=10:
    #     #     pass
    #     # print(cam.camera.GetQueuedBufferCount(), 'f'*100)
    #     # print('-'*100)
    # # func = get_threading(cameras)
    # # func()
