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
from PyQt5.QtCore import QTimer
from pypylon import genicam

DEBUG = False

import database_utils

show_eror = False

if show_eror:

    from eror_window import UI_eror_window


class Collector():

    def __init__(self, serial_number,gain = 0 , exposure = 70000, max_buffer = 20, trigger=True, delay_packet=100, packet_size=1500 ,
                frame_transmission_delay=0 ,width=1000,height=1000,offet_x=0,offset_y=0, manual=False, list_devices_mode=False, trigger_source='Software'):
        """Initializes the Collector
        Args:
            gain (int, optional): The gain of images. Defaults to 0.
            exposure (float, optional): The exposure of the images. Defaults to 3000.
            max_buffer (int, optional): Image buffer for cameras. Defaults to 5.
        """
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

        if show_eror:
            self.window_eror = UI_eror_window()

        self.__tl_factory = pylon.TlFactory.GetInstance()
        devices = []


        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned


        for device in self.__tl_factory.EnumerateDevices():
            if (device.GetDeviceClass() == 'BaslerGigE'):                
                devices.append(device)

        # assert len(devices) > 0 , 'No Camera is Connected!
        if self.list_devices_mode:
            self.cameras = list()

            for device in devices:
                camera = pylon.InstantCamera(self.__tl_factory.CreateDevice(device))
                self.cameras.append(camera)
        
        else:
            for device in devices:
                camera = pylon.InstantCamera(self.__tl_factory.CreateDevice(device))
                print(camera.GetDeviceInfo().GetSerialNumber())
                if camera.GetDeviceInfo().GetSerialNumber() == self.serial_number:
                    self.camera = camera
                
                    break

        #assert len(devices) > 0 , 'No Camera is Connected!'
        
        self.caprturing_timer = QTimer()
        self.caprturing_timer.timeout.connect(self.getPictures)

    
    def add_triger_function(self,trig_func):
        self.trig_func = trig_func

    def eror_window(self,msg,level):
        self.window_eror = UI_eror_window()
       # self.ui2= UI_eror_window()
        self.window_eror.show()
        self.window_eror.set_text(msg,level)


    def tempreture(self):
        device_info = self.camera.GetDeviceInfo()
        model=str(device_info.GetModelName())
        model=model[-3:]
        if model=='PRO':
            # print(self.camera.DeviceTemperature.GetValue())
            return self.camera.DeviceTemperature.GetValue()
        else :
            # print('temp',self.camera.TemperatureAbs.GetValue())
            return self.camera.TemperatureAbs.GetValue()


    def start_grabbing(self):

        device_info = self.camera.GetDeviceInfo()
        model=str(device_info.GetModelName())
        model=model[-3:]
        # print(model[-3:])


        try:
            print(self.camera.IsOpen())
            print(device_info.GetSerialNumber())

            self.camera.Open()
            
            if self.manual:

                
                if model=='PRO':
                    print('yes pro')
                    # print(self.camera.DeviceTemperature.GetValue())
                    self.camera.ExposureTime.SetValue(self.exposure)

                    self.camera.Gain.SetValue(self.gain)
                    
                    # self.camera.GevSCPSPacketSize.SetValue(int(self.ps)+1000)
                    # self.camera.Close()
                    # self.camera.Open()
                    self.camera.GevSCPSPacketSize.SetValue(int(self.ps))
                    self.camera.Close()
                    self.camera.Open()
                                                  
                    self.camera.GevSCPD.SetValue(self.dp)
                    self.camera.Close()
                    self.camera.Open()                   
                    self.camera.GevSCFTD.SetValue(self.ftd)
                    self.camera.Close()
                    self.camera.Open()




                    self.camera.Width.SetValue(self.width)
                    self.camera.Height.SetValue(self.height)

                    self.camera.OffsetX.SetValue(self.offset_x)
                    self.camera.OffsetY.SetValue(self.offset_y)
                    



                

                else:
                    


                    self.camera.ExposureTimeAbs.SetValue(self.exposure)
                    self.camera.GainRaw.SetValue(self.gain)

                    self.camera.GevSCPSPacketSize.SetValue(int(self.ps)+1000)
                    self.camera.Close()
                    self.camera.Open()
                                
                    self.camera.GevSCPD.SetValue(self.dp)
                    self.camera.Close()
                    self.camera.Open()                   
                    self.camera.GevSCFTD.SetValue(self.ftd)
                    self.camera.Close()
                    self.camera.Open()

                    self.camera.GevSCPSPacketSize.SetValue(int(self.ps))
                    self.camera.Close()
                    self.camera.Open()
                    self.camera.Width.SetValue(self.width)
                    self.camera.Height.SetValue(self.height)

                    self.camera.OffsetX.SetValue(self.offset_x)
                    self.camera.OffsetY.SetValue(self.offset_y)
                    


            self.camera.Close()

            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 

            self.camera.Open()

            if self.trigger:
                self.camera.TriggerSelector.SetValue('FrameStart')
                self.camera.TriggerMode.SetValue('On')
                self.camera.TriggerSource.SetValue(self.trigger_source)
                print('triggeron on %s' % self.trigger_source)
            else:
                # self.camera.TriggerMode.SetValue('Off')
                print('triggeroff')

            # if self.manual:
            #     self.camera.ExposureTimeAbs.SetValue(20000)


            #     # self.camera.Width.SetValue(600)
            #     print(self.camera.Width.GetValue())
            #     self.camera.Width.SetValue(600)
            #     # int64_t = self.camera.PayloadSize.GetValue()
            #     # self.camera.GevStreamChannelSelectorCamera.GevStreamChannelSelector.SetValue( 'GevStreamChannelSelector_StreamChannel0 ')
            #     # self.camera.GevSCPSPacketSize.SetValue(1500)
                             
            #     self.camera.GevSCPD.SetValue(self.dp)
                
            #     self.camera.GevSCFTD.SetValue(self.ftd)
            self.exitCode=0

            return True, 'start grabbing ok'
            
        except genicam.GenericException as e:
            # Error handling
            
            message = self.start_grabbing_error_handling(error=e)
            #print(e)  
        
            self.stop_grabbing()
            #print("An exception occurred.", e.GetDescription())
            self.exitCode = 1
            # self.eror_window('Check The Number of cameras',3)

            
            return False, message

    
    def start_grabbing_error_handling(self, error):
        message = ''
        # camera in use
        if 'The device is controlled by another application' in str(error):
            message = 'Camera is controlled by another application'

        # expossure invalid
        elif "OutOfRangeException thrown in node 'ExposureTimeAbs' while calling 'ExposureTimeAbs.SetValue()" in str(error):
            # min
            if 'greater than or equal' in str(error):
                message = 'Exposure value is too small'
            elif 'must be smaller than or equal' in str(error):
                message = 'Exposure value is too large'
            else:
                message = 'Exposure value invalid'

        # gain invalid
        elif "OutOfRangeException thrown in node 'GainRaw' while calling 'GainRaw.SetValue()" in str(error):
            if 'must be equal or greater than' in str(error):
                message = 'Gain value is too small'
            elif 'must be equal or smaller than' in str(error):
                message = 'Gain value is too large'
            else:
                message = 'Gain value invalid'

        # packetsize invalid
        elif "OutOfRangeException thrown in node 'GevSCPSPacketSize' while calling 'GevSCPSPacketSize.SetValue()" in str(error):
            message = 'Packet-size value invalid'
        
        # transmission delay
        elif "OutOfRangeException thrown in node 'GevSCFTD' while calling 'GevSCFTD.SetValue()" in str(error):
            if 'must be equal or greater than' in str(error):
                message = 'Transmision delay is too small'
            elif 'must be equal or smaller than' in str(error):
                message = 'Transmision delay is too large'
            else:
                message = 'Transmision delay value invalid'

        # height delay
        elif "OutOfRangeException thrown in node 'Height' while calling 'Height.SetValue()" in str(error):
            if 'must be equal or greater than' in str(error):
                message = 'Height value is too small'
            elif 'must be equal or smaller than' in str(error):
                message = 'Height value is too large'
            else:
                message = 'Height value invalid'

        # width delay
        elif "OutOfRangeException thrown in node 'Width' while calling 'Width.SetValue()" in str(error):
            if 'must be equal or greater than' in str(error):
                message = 'Width value is too small'
            elif 'must be equal or smaller than' in str(error):
                message = 'Width value is too large'
            else:
                message = 'Width value invalid'

        # offsetx delay
        elif "OutOfRangeException thrown in node 'OffsetX' while calling 'OffsetX.SetValue()" in str(error):
            if 'must be equal or greater than' in str(error):
                message = 'Offsetx value is too small'
            elif 'must be equal or smaller than' in str(error):
                message = 'Offsetx value is too large'
            else:
                message = 'Offsetx value invalid'

        # offsety delay
        elif "OutOfRangeException thrown in node 'OffsetY' while calling 'OffsetY.SetValue()" in str(error):
            if 'must be equal or greater than' in str(error):
                message = 'Offsety value is too small'
            elif 'must be equal or smaller than' in str(error):
                message = 'Offsety value is too large'
            else:
                message = 'Offsety value invalid'
        

        else:
            message = str(error)

        return message



    def stop_grabbing(self):
        self.camera.Close()

            
        
    def listDevices(self):
        """Lists the available devices
        """
        for i ,  camera in enumerate(self.cameras):
            device_info = camera.GetDeviceInfo()
            print(
                "Camera #%d %s @ %s (%s) @ %s" % (
                i,
                device_info.GetModelName(),
                device_info.GetIpAddress(),
                device_info.GetMacAddress(),
                device_info.GetSerialNumber(),
                )
            
            )
            print(device_info)


    def serialnumber(self):
        serial_list=[]
        for i ,  camera in enumerate(self.cameras):
            device_info = camera.GetDeviceInfo()
            serial_list.append(device_info.GetSerialNumber())
        return serial_list         




    def trigg_exec(self,):
        
        if self.trigger:
            self.camera.TriggerSoftware()
            #print(self.camera.GetQueuedBufferCount(), 'T'*100)
            while self.camera.GetQueuedBufferCount() >=10:
                pass
            #print(self.camera.GetQueuedBufferCount(), 'T'*100)


    def getPictures(self, time_out = 50):
        Flag=True
        try:

            
            if DEBUG:
                print('TRIGE Done')
            # print('444444444444', self.camera.IsGrabbing())
            if self.camera.IsGrabbing():
                if DEBUG:
                    print('Is grabbing')
                    
                    if self.camera.GetQueuedBufferCount() == 10:
                        print('ERRRRRRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRRRRRR')
                grabResult = self.camera.RetrieveResult(time_out, pylon.TimeoutHandling_ThrowException)

                # print('grab',grabResult)
                

                # print(self.camera.GetQueuedBufferCount(), 'f'*100)
                if DEBUG:
                    print('RetrieveResult')

                    if self.camera.GetQueuedBufferCount() == 10:
                        print('ERROR!: Buffer')
                if grabResult.GrabSucceeded():
                    
                    if DEBUG:
                        print('Grab Succed')

                    image = self.converter.Convert(grabResult)
                    img=image.Array
                    self.trig_func(img)

                else:
                    img=np.zeros([1200,1920,3],dtype=np.uint8)
                    self.cont_eror+=1
                    #print('eror',self.cont_eror)
                    print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
                    Flag=False

            else:
                    print('Error!: Camera not Grabbing')
                    img=np.zeros([1200,1920,3],dtype=np.uint8)
                    Flag=False

        except:
            #print('Time out')
            img=np.zeros([1200,1920,3],dtype=np.uint8)
            Flag=False

        # cv2.imshow("img1", cv2.resize(img, None, fx=0.5, fy=0.5))
        # cv2.waitKey(50)
        if Flag:
            #print('yes')
            return True, img
        else:
            #print('no')
            return False, np.zeros([1200,1920,3],dtype=np.uint8)



    def continiuse_capturing(self):
        self.caprturing_timer.start()



    def get_cam(self,i):
        return self.camera
    


def get_all_devices():

    tl_factory = pylon.TlFactory.GetInstance()

    cam = None
    # tlf = pylon.TlFactory.GetInstance()

    # for tl in tlf.EnumerateTls():
    #     print(tl.GetDeviceClass(), tl.GetFileName(), tl.GetFullName())
    for dev_info in tl_factory.EnumerateDevices():
        if dev_info.GetDeviceClass() == "BaslerGigE":
            print("using %s @ %s" % (dev_info.GetModelName(), dev_info.GetIpAddress()))
            cam = pylon.InstantCamera(tl_factory.CreateDevice(dev_info))
            # break
    return False


if __name__ == "__main__":


    collector = Collector(
        "24350367",
        exposure=3000,
        gain=10,
        trigger=False,
        delay_packet=81062,
        packet_size=9000,
        frame_transmission_delay=18036,
        height=1000,
        width=1000,
        offet_x=16,
        offset_y=4,
        manual=False,
    )

    # x=collector.get_cam()

    # collector.start_grabbing()
    # collector.start_grabbing()
    cameras = collector

    cameras.start_grabbing()
    cameras.getPictures()
    # print(cameras.)

    while True:

        #     # for cam in cameras:
        #     #         cam.trigg_exec()

        #     # for cam in cameras:
        #     #print(cam.camera.GetQueuedBufferCount())
        img = cameras.getPictures()
        img=img[1]
        print(img.shape)
        # print(cam.camera.GetQueuedBufferCount())
        cv2.imshow("img1", cv2.resize(img, None, fx=0.5, fy=0.5))
        img=np.uint8(img)
        # cv2.imshow('img',img)
        cv2.waitKey(50)
