-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: screw
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `camera_settings`
--

DROP TABLE IF EXISTS `camera_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `camera_settings` (
  `id` int DEFAULT NULL,
  `gain_top` int DEFAULT NULL,
  `gain_bottom` int DEFAULT NULL,
  `gain_value` int DEFAULT NULL,
  `expo_top` int DEFAULT NULL,
  `expo_bottom` int DEFAULT NULL,
  `expo_value` int DEFAULT NULL,
  `width` int DEFAULT NULL,
  `height` int DEFAULT NULL,
  `offsetx_top` int DEFAULT NULL,
  `offsetx_bottom` int DEFAULT NULL,
  `offsetx_value` int DEFAULT NULL,
  `offsety_top` int DEFAULT NULL,
  `offsety_bottom` int DEFAULT NULL,
  `offsety_value` int DEFAULT NULL,
  `interpacket_delay` int DEFAULT NULL,
  `packet_size` int DEFAULT NULL,
  `trigger_mode` int DEFAULT NULL,
  `max_buffer` int DEFAULT NULL,
  `transmission_delay` int DEFAULT NULL,
  `ip_address` text,
  `rotation_value` double DEFAULT NULL,
  `shifth_value` int DEFAULT NULL,
  `shiftw_value` int DEFAULT NULL,
  `serial_number` int DEFAULT NULL,
  `pxvalue_a` double DEFAULT NULL,
  `pxvalue_b` double DEFAULT NULL,
  `pxvalue_c` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camera_settings`
--

LOCK TABLES `camera_settings` WRITE;
/*!40000 ALTER TABLE `camera_settings` DISABLE KEYS */;
INSERT INTO `camera_settings` VALUES (1,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,14,10,'192.168.1.100',3.7,-39,2,0,0,0,0),(2,0,360,0,35,10000000,3000,1920,1195,16,0,0,16,0,0,0,0,1,0,0,'',0,0,0,0,0,0,0),(3,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(4,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(5,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',2,21,50,0,0,0,0),(6,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(7,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(8,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(9,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(10,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(11,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(12,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(13,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(14,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(15,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(16,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(17,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(18,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(19,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(20,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(21,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(22,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(23,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0),(24,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `camera_settings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-28 20:54:38