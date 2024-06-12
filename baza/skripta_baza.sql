-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: blank_space
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add zanr',7,'add_zanr'),(26,'Can change zanr',7,'change_zanr'),(27,'Can delete zanr',7,'delete_zanr'),(28,'Can view zanr',7,'view_zanr'),(29,'Can add pesma',8,'add_pesma'),(30,'Can change pesma',8,'change_pesma'),(31,'Can delete pesma',8,'delete_pesma'),(32,'Can view pesma',8,'view_pesma'),(33,'Can add izvodjac',9,'add_izvodjac'),(34,'Can change izvodjac',9,'change_izvodjac'),(35,'Can delete izvodjac',9,'delete_izvodjac'),(36,'Can view izvodjac',9,'view_izvodjac'),(37,'Can add predlaze_ izvodjaca',10,'add_predlaze_izvodjaca'),(38,'Can change predlaze_ izvodjaca',10,'change_predlaze_izvodjaca'),(39,'Can delete predlaze_ izvodjaca',10,'delete_predlaze_izvodjaca'),(40,'Can view predlaze_ izvodjaca',10,'view_predlaze_izvodjaca'),(41,'Can add soba',11,'add_soba'),(42,'Can change soba',11,'change_soba'),(43,'Can delete soba',11,'delete_soba'),(44,'Can view soba',11,'view_soba'),(45,'Can add stihovi',12,'add_stihovi'),(46,'Can change stihovi',12,'change_stihovi'),(47,'Can delete stihovi',12,'delete_stihovi'),(48,'Can view stihovi',12,'view_stihovi'),(49,'Can add predlaze_ pesmu',13,'add_predlaze_pesmu'),(50,'Can change predlaze_ pesmu',13,'change_predlaze_pesmu'),(51,'Can delete predlaze_ pesmu',13,'delete_predlaze_pesmu'),(52,'Can view predlaze_ pesmu',13,'view_predlaze_pesmu'),(53,'Can add korisnik',14,'add_korisnik'),(54,'Can change korisnik',14,'change_korisnik'),(55,'Can delete korisnik',14,'delete_korisnik'),(56,'Can view korisnik',14,'view_korisnik');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$5JtlAI71hAGJ6jgMWtfgKX$LQ6pApwLDTbepsU6Tamd7Wu7yeUEtDuTkrGbP4rBjoU=','2024-05-18 10:16:19.712334',1,'jana','','','stanisavljevicj.js@gmail.com',1,1,'2024-05-18 10:15:54.175601');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'appBlankSpace','izvodjac'),(14,'appBlankSpace','korisnik'),(8,'appBlankSpace','pesma'),(10,'appBlankSpace','predlaze_izvodjaca'),(13,'appBlankSpace','predlaze_pesmu'),(11,'appBlankSpace','soba'),(12,'appBlankSpace','stihovi'),(7,'appBlankSpace','zanr'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'appBlankSpace','0001_initial','2024-05-01 16:16:10.613527'),(2,'contenttypes','0001_initial','2024-05-03 13:45:09.780602'),(3,'auth','0001_initial','2024-05-03 13:45:10.492943'),(4,'admin','0001_initial','2024-05-03 13:45:10.650400'),(5,'admin','0002_logentry_remove_auto_add','2024-05-03 13:45:10.660404'),(6,'admin','0003_logentry_add_action_flag_choices','2024-05-03 13:45:10.668659'),(7,'contenttypes','0002_remove_content_type_name','2024-05-03 13:45:10.771661'),(8,'auth','0002_alter_permission_name_max_length','2024-05-03 13:45:10.889760'),(9,'auth','0003_alter_user_email_max_length','2024-05-03 13:45:10.950527'),(10,'auth','0004_alter_user_username_opts','2024-05-03 13:45:10.964317'),(11,'auth','0005_alter_user_last_login_null','2024-05-03 13:45:11.055000'),(12,'auth','0006_require_contenttypes_0002','2024-05-03 13:45:11.058704'),(13,'auth','0007_alter_validators_add_error_messages','2024-05-03 13:45:11.074672'),(14,'auth','0008_alter_user_username_max_length','2024-05-03 13:45:11.201254'),(15,'auth','0009_alter_user_last_name_max_length','2024-05-03 13:45:11.275563'),(16,'auth','0010_alter_group_name_max_length','2024-05-03 13:45:11.320520'),(17,'auth','0011_update_proxy_permissions','2024-05-03 13:45:11.344630'),(18,'auth','0012_alter_user_first_name_max_length','2024-05-03 13:45:11.431660'),(19,'sessions','0001_initial','2024-05-03 13:45:11.467304'),(20,'appBlankSpace','0002_korisnik_izvodjac_pesma_predlaze_izvodjaca_and_more','2024-05-03 14:39:43.045984'),(21,'appBlankSpace','0003_rename_id_zan_izvodjac_zan_rename_id_izv_pesma_izv_and_more','2024-05-03 14:42:16.129960'),(22,'appBlankSpace','0004_alter_korisnik_licni_poeni_and_more','2024-05-03 15:29:30.080497'),(23,'appBlankSpace','0005_alter_stihovi_zvuk','2024-05-03 16:16:30.197592'),(24,'appBlankSpace','0006_alter_soba_kor_2','2024-05-04 10:12:17.688364'),(25,'appBlankSpace','0007_soba_poeni_1_soba_poeni_2_soba_runda','2024-05-04 12:27:54.969900'),(26,'appBlankSpace','0008_remove_soba_runda','2024-05-04 13:32:46.834629'),(27,'appBlankSpace','0009_soba_poeni_runde_1_soba_poeni_runde_2','2024-05-05 08:23:51.272780'),(28,'appBlankSpace','0010_soba_pesme','2024-05-07 08:31:52.680668'),(29,'appBlankSpace','0011_rename_pesme_soba_stihovi','2024-05-07 08:31:52.693667'),(30,'appBlankSpace','0012_alter_soba_stihovi','2024-05-07 08:31:52.731042'),(31,'appBlankSpace','0013_alter_soba_stihovi','2024-05-07 09:05:50.377946'),(32,'appBlankSpace','0014_korisnik_odgovor_lozinka_korisnik_pitanje_lozinka','2024-05-16 08:28:00.425727'),(33,'appBlankSpace','0015_alter_soba_kor_1','2024-05-17 22:03:27.731972'),(34,'appBlankSpace','0016_alter_soba_poeni_1_alter_soba_poeni_2','2024-05-18 06:56:54.935681'),(35,'appBlankSpace','0017_alter_soba_poeni_2','2024-05-18 07:19:33.654747');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('f9pvzb31s2nz1etmsrq4mxswzyeezdg3','eyJrb3JpbWUiOiJnaWNhIn0:1sAt2L:X38nvBaSEaq_TmHvyaLrX9HHytmJ7JNPZ2g861TFK4o','2024-06-01 15:10:21.305124');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `izvodjac`
--

DROP TABLE IF EXISTS `izvodjac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `izvodjac` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ime` varchar(31) NOT NULL,
  `zan_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `izvodjac_zan_id_31fbace1_fk_zanr_id` (`zan_id`),
  CONSTRAINT `izvodjac_zan_id_31fbace1_fk_zanr_id` FOREIGN KEY (`zan_id`) REFERENCES `zanr` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `izvodjac`
--

LOCK TABLES `izvodjac` WRITE;
/*!40000 ALTER TABLE `izvodjac` DISABLE KEYS */;
INSERT INTO `izvodjac` VALUES (1,'Taylor Swift',1),(2,'Harry Styles',1),(3,'Lady Gaga',1),(4,'Britney Spears',1),(5,'Post Malone',1),(6,'Rozga',2),(7,'Severina',2),(8,'Zdravko Čolić',2),(9,'Balašević',2),(10,'Željko Joksimović',2),(11,'Ceca',3),(12,'Lepa Brena',3),(13,'Aleksandra Prijović',3),(14,'Aco Pejović',3),(15,'Željko Samardžić',3),(16,'Silvana',4),(17,'Ana Bekuta',4),(18,'Zorica Brunclik',4),(19,'Toma Zdravković',4),(20,'Džej',4),(21,'Nicky',5),(22,'Iggy Azalea',5),(23,'Cardi B',5),(24,'Drake',5),(25,'Jay-Z',5);
/*!40000 ALTER TABLE `izvodjac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnicko_ime` varchar(31) NOT NULL,
  `sifra` varchar(255) NOT NULL,
  `ime` varchar(31) NOT NULL,
  `prezime` varchar(31) NOT NULL,
  `tip` varchar(1) NOT NULL,
  `rang_poeni` int DEFAULT NULL,
  `licni_poeni` int DEFAULT NULL,
  `poslednja_aktivnost` datetime(6) DEFAULT NULL,
  `odgovor_lozinka` varchar(255) NOT NULL,
  `pitanje_lozinka` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (1,'sojic','pbkdf2_sha256$720000$LrETqAgbvBFtCgGW8tWFUA$626mP8WmQ2T6EvPX1AB9YZPawhhZr5oWb+GqbUnMPdM=','Srećko','Šojić','S',50,70,'2024-04-11 01:02:02.000000','pbkdf2_sha256$720000$wkIJ30UQKFpdXimvMUGsPb$S+fSpCc9/vXPHKxApo52LOJ28cDKBtVPWenyyMG/Exo=','Ime prvog kućnog ljubimca?'),(2,'sin_dragan','pbkdf2_sha256$720000$YlyhAU26cQ2YZXeDEqLFmo$mDUMOSnCdQgnd/9sr8hGW+zXgX+sCJz7iwzkKukQe5s=','Dragan','Raković','B',20,22,'2024-04-06 06:30:00.000000','pbkdf2_sha256$720000$yd4pYH7PP87zsh4Qz5PBAu$K38kLaHrpeBgj5a0ABtL70YumuVuPnL6yuiBltKsSc8=','Ime prvog kućnog ljubimca?'),(3,'surda','pbkdf2_sha256$720000$MNjc5lN67nyAvMxhGeJKI9$KP/2/WoJ77kA794KaihzWXajHsVwh2DhkR5F91nbU0Q=','Borivoje','Šurdilović','S',24,55,'2024-04-09 03:20:00.000000','pbkdf2_sha256$720000$UJtTAkQTXzi799RHvbJASf$S1+TI8an9jKJVlwOStX/rPalp6Y4Dsuzkpvh922kEJA=','Ime prvog kućnog ljubimca?'),(4,'jare','pbkdf2_sha256$720000$ksilOfBZU41Mg2RcynP0CY$1ai/j+M3qgcKychIJsMLiV34pS1DvzmQN+ufqDG1o8U=','Živadin','Jarić','S',53,56,'2024-04-01 18:02:00.000000','pbkdf2_sha256$720000$wvSg6E2SY9QUCHSPQ5W6cs$4novDn2WExlWsLcbgS6Vtq8GwMUtVS5DC5eY6XL9O08=','Ime prvog kućnog ljubimca?'),(5,'gojko','pbkdf2_sha256$720000$mZpPBtcuw2zogzpY7q8tKu$q45ta8rDjO024XSSHr55rG1XA52ISF13t/to+ViZC38=','Gojko','Marić','M',12,123,'2024-03-11 00:00:00.000000','pbkdf2_sha256$720000$jAP9ajqVf1dT3BoF06EwOp$ce7k6BvpRJyjp52T5Soe5LawNr1TxRQM919iMKl20yE=','Ime prvog kućnog ljubimca?'),(6,'gigamoravac','pbkdf2_sha256$720000$EZnQwyIm01i64CTTluYEna$NktUPr+Q0/jkADKwJfbuh2ir7389wP2W/MpPsHM1qBg=','Dragiša','Popadić','M',6,134,'2024-03-18 00:00:00.000000','pbkdf2_sha256$720000$6tJ2ml0QIrz5yUFuwqEPr9$JA/C5thOwIXUY26ZNBncsJOvWfDjG4mREX513tjsQO8=','Ime prvog kućnog ljubimca?'),(7,'tika','pbkdf2_sha256$720000$peIay3q1HWcTSkYBb6YCKG$CVgNBW91iBfSuNlgR0iysXC7VqxmZu+GGO7bR/GckKA=','Tihomir','Stojković','S',65,89,'2024-04-03 10:00:00.000000','pbkdf2_sha256$720000$nn3nKnYu6Imz3VIGCSthfr$sHG8EHtL2462jr3eGCK60fk3+WP5R3iywqb9K7cC/r4=','Ime prvog kućnog ljubimca?'),(8,'ilija','pbkdf2_sha256$720000$KnzyyOnuTs8nfTJTdOkyhQ$1W8M0dGlyOr74AuJ2RVxG4hrMMryaUUg+AiQOAXETH0=','Ilija','Čvorović','B',12,35,'2024-04-11 01:00:00.000000','pbkdf2_sha256$720000$oPfRTNnAAnuRl4SjxX98Ai$WsS7231qCQkjdXkG7gIZObqHY0wuq1oiD3lvcOebBig=','Ime prvog kućnog ljubimca?'),(9,'tajson','pbkdf2_sha256$720000$L5NVppMsrpqwIs1ssK5Q53$iZZfSnUZxFcs/bBaAM/lqNV8GSQOdCWcaPMRMEIIM/I=','Slobodan','Tanasijević','B',10,12,'2024-04-11 03:00:00.000000','pbkdf2_sha256$720000$YipiVzeuHwpdvCPMoKKOY3$uSxOnsxNKZmjP9i1oBioFrw/+H53Bs2sy+gQPfOXUBk=','Ime prvog kućnog ljubimca?'),(10,'evgenije','pbkdf2_sha256$720000$rEQZvJMOl5uxNY20IvxiXG$/PCReAd+9a9aOWXXpa/kBgvKkeje7z5C+v4L/Sq0sGU=','Evgenije','Onjegin','S',8,65,'2024-04-05 00:00:00.000000','pbkdf2_sha256$720000$rNFIdJcxh3Kt3ovZLPqHQI$P9AdB+rycQ7RCKDlPPyJqSfvO4kSWLUHNPjlzBs24z0=','Ime prvog kućnog ljubimca?'),(11,'zona','pbkdf2_sha256$720000$tTYqTd0TaLGPt7Mzt17v2M$vcEzroYFhyibqgna1nCLL5Ct7FPdUIpRX+fOEHJOlD4=','Zona','Zamfirova','B',34,48,'2024-03-01 07:50:00.000000','pbkdf2_sha256$720000$YXFNX2MQSCi4ahjL5pybgV$XMXeCgbC8YjgV5svB7WSAZ4IOOM0Qe7t8mDOljtOPC0=','Ime prvog kućnog ljubimca?'),(12,'poaro','pbkdf2_sha256$720000$ZLWZ56s28bw71tDsee7rzd$TFex8jeZE1QKi70JRFED4ZIz3mgRNtG6IANubttofgk=','Herkul','Poaro','B',30,36,'2024-03-26 02:40:00.000000','pbkdf2_sha256$720000$AqIOq7NtIS77gSYf8LPXqP$qznZmfq1we7M7wS950J5u8R9LtCoYBgEG8WL6QplW0M=','Ime prvog kućnog ljubimca?'),(13,'ana','pbkdf2_sha256$720000$gDshCWBbIICACHL64vVBuV$cUKLcH9WnViXdQG9q4p01PGSDv+wwKNXVCixLA/nkeU=','Ana','Karenjina','M',23,133,'2024-04-05 00:00:00.000000','pbkdf2_sha256$720000$NMF8REycV2eo1GPCR3SIdo$fPich3E40yrFRwpJAZOAytvCUYBqlV+H84JDQ1wL1wg=','Ime prvog kućnog ljubimca?'),(14,'dusko','pbkdf2_sha256$720000$6BUlpcTz3VjuGZF6QlZaHm$cVY6eZu48OwA/UIw65upryoNfTQDahx5jcdX7sL0/gM=','Duško','Dugouško','S',17,97,'2024-04-03 00:00:00.000000','pbkdf2_sha256$720000$QphRVrONpW9rW8gaFxs5Xy$HWtMOcHt+YnNmkk58EcZbG338tEVKr80VJy4b/5o4j8=','Ime prvog kućnog ljubimca?'),(15,'gica','pbkdf2_sha256$720000$i8aPj1DEKzebytrDbOtyWL$66rwHaE427KrWXyUDhWSRSm0tNf5ygJTNJ2cPe2WNMg=','Gica','Prasić','B',5,15,'2024-04-02 03:00:00.000000','pbkdf2_sha256$720000$3BJsfdpO9Uv1JAVsQueam8$H+QgRIaaoS+mriHLYPe3KNnqS0ozMZXs1lX4ve7V3+w=','Ime prvog kućnog ljubimca?'),(46,'bond','pbkdf2_sha256$720000$dtQsDMXhhVg42GhZ1mTCqD$X7b/VCCCnxzLa/ciomxPA803Wf/dU1fHc+0+wNbAFOw=','James','Bond','A',NULL,NULL,NULL,'pbkdf2_sha256$720000$GvDCO4lm6Oj94WwTbvUfA8$b54Fde/iNvO7aB34WfpxrtAiY68wvy0T3geyplPAJoc=','Ime prvog kućnog ljubimca?'),(47,'mrBean','pbkdf2_sha256$720000$FkoylQzTBotvM5TwNgFPfg$mmKdmrftHKjgXOHqTHD3rCIvlKfMyvflFjPCoZbm7U8=','Mr','Bean','A',NULL,NULL,NULL,'pbkdf2_sha256$720000$pPkKFrtnxO9BuaVzM69XSv$NtXpdMIl1FS3B4thz5EYNvKWq8rO+z/LNzU3L/zzUoM=','Ime prvog kućnog ljubimca?');
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pesma`
--

DROP TABLE IF EXISTS `pesma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pesma` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `naziv` varchar(63) NOT NULL,
  `izv_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pesma_izv_id_6c08dcaf_fk_izvodjac_id` (`izv_id`),
  CONSTRAINT `pesma_izv_id_6c08dcaf_fk_izvodjac_id` FOREIGN KEY (`izv_id`) REFERENCES `izvodjac` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pesma`
--

LOCK TABLES `pesma` WRITE;
/*!40000 ALTER TABLE `pesma` DISABLE KEYS */;
INSERT INTO `pesma` VALUES (1,'Blank Space',1),(3,'All too well',1),(4,'Style',1),(5,'Sign of the Times',2),(6,'Adore you',2),(7,'Matilda',2),(8,'Circles',5),(9,'Goodbyes',5),(10,'Better Now',5),(11,'Legitimno',13),(12,'Ja sam odlicno',13),(13,'Psiho',13),(14,'Bodak Yellow',23),(15,'I Like it',23),(16,'Money',23),(17,'One Dance',24),(18,'God\'s Plan',24),(19,'Hotline Bling',24),(20,'Empire State Of Mind',25),(21,'Young Forever',25),(22,'Already Home',25),(23,'Alejandro',3),(24,'Bad Romance',3),(25,'Blago meni',17),(26,'Bože Bože',18),(27,'Criminal',4),(28,'Da raskinem sa njom',11),(29,'Hold It Against Me',4),(30,'Ime i prezime',11),(31,'Kada bi me pitali',18),(32,'Kralj ponoći',17),(33,'Pao mrak',17),(34,'Personal Problem',22),(35,'Savior',22),(36,'Starships',21),(37,'Tamo gde si ti',18),(38,'Team',22),(39,'Toxic',4),(40,'Trazio si sve',11),(41,'Va Va Voom',21),(42,'Young Forever',21),(43,'Da si tu',14),(44,'Oko mene',14),(45,'Sve ti dugujem',14),(46,'Ne lomite mi bagrenje',9),(47,'Ringišpil',9),(48,'Svirajte mi jesen stiže dunjo moja',9),(49,'Jugoslovenka',12),(50,'Sanjam',12),(51,'Udji slobodno',12),(52,'Kao moja mati',8),(53,'Produži dalje',8),(54,'Sačuvaj me bože njene ljubavi',8),(55,'Gde ću sad, moja ružo',20),(56,'Imati pa nemati',20),(57,'Nedelja',20),(58,'Bižuterija',6),(59,'Kad bi bio blizu',6),(60,'Minus i plus',6),(61,'Idu dani',10),(62,'Michelle',10),(63,'Zaboravljaš',10),(64,'Ako odeš',15),(65,'Bezobrazno zelene',15),(66,'Grlica',15),(67,'Bradd Pitt',7),(68,'Dobrodošao u klub',7),(69,'Grad bez ljudi',7),(70,'A što ćemo ljubav kriti',16),(71,'Ciganine, sviraj, sviraj',16),(72,'Rane moje',16),(73,'Pesme moje',19),(74,'Šta će mi život',19),(75,'Svirajte mi tiho tiše',19),(76,'Za Ljiljanu',19);
/*!40000 ALTER TABLE `pesma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `predlaze_izvodjaca`
--

DROP TABLE IF EXISTS `predlaze_izvodjaca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `predlaze_izvodjaca` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ime_izvodjaca` varchar(31) NOT NULL,
  `kor_id` bigint NOT NULL,
  `zan_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `predlaze_izvodjaca_kor_id_762ddced_fk_korisnik_id` (`kor_id`),
  KEY `predlaze_izvodjaca_zan_id_04382263_fk_zanr_id` (`zan_id`),
  CONSTRAINT `predlaze_izvodjaca_kor_id_762ddced_fk_korisnik_id` FOREIGN KEY (`kor_id`) REFERENCES `korisnik` (`id`) ON DELETE CASCADE,
  CONSTRAINT `predlaze_izvodjaca_zan_id_04382263_fk_zanr_id` FOREIGN KEY (`zan_id`) REFERENCES `zanr` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `predlaze_izvodjaca`
--

LOCK TABLES `predlaze_izvodjaca` WRITE;
/*!40000 ALTER TABLE `predlaze_izvodjaca` DISABLE KEYS */;
INSERT INTO `predlaze_izvodjaca` VALUES (1,'Vlado Georgiev',1,2),(2,'Justin Bieber',3,1),(3,'Miki Jevremović',13,2),(4,'Halid Bešlić',14,4);
/*!40000 ALTER TABLE `predlaze_izvodjaca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `predlaze_pesmu`
--

DROP TABLE IF EXISTS `predlaze_pesmu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `predlaze_pesmu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `naziv_pesme` varchar(63) NOT NULL,
  `izv_id` bigint NOT NULL,
  `kor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `predlaze_pesmu_izv_id_abbee737_fk_izvodjac_id` (`izv_id`),
  KEY `predlaze_pesmu_kor_id_a7b96a4d_fk_korisnik_id` (`kor_id`),
  CONSTRAINT `predlaze_pesmu_izv_id_abbee737_fk_izvodjac_id` FOREIGN KEY (`izv_id`) REFERENCES `izvodjac` (`id`) ON DELETE CASCADE,
  CONSTRAINT `predlaze_pesmu_kor_id_a7b96a4d_fk_korisnik_id` FOREIGN KEY (`kor_id`) REFERENCES `korisnik` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `predlaze_pesmu`
--

LOCK TABLES `predlaze_pesmu` WRITE;
/*!40000 ALTER TABLE `predlaze_pesmu` DISABLE KEYS */;
INSERT INTO `predlaze_pesmu` VALUES (1,'Dotakao sam dno života',19,13),(2,'Ne volim januar',9,5),(3,'22',1,6),(4,'Kafana je moja istina',19,13),(5,'Two Ghosts',2,5),(6,'Duet',9,6),(7,'Kiwi',2,13),(8,'Slavija',20,5);
/*!40000 ALTER TABLE `predlaze_pesmu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soba`
--

DROP TABLE IF EXISTS `soba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soba` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `kor_1_id` bigint DEFAULT NULL,
  `kor_2_id` bigint DEFAULT NULL,
  `poeni_1` int NOT NULL,
  `poeni_2` int DEFAULT NULL,
  `poeni_runde_1` varchar(31) DEFAULT NULL,
  `poeni_runde_2` varchar(31) DEFAULT NULL,
  `stihovi` varchar(63) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soba_kor_1_id_99024be6_fk_korisnik_id` (`kor_1_id`),
  KEY `soba_kor_2_id_6e43d84a_fk_korisnik_id` (`kor_2_id`),
  CONSTRAINT `soba_kor_1_id_99024be6_fk_korisnik_id` FOREIGN KEY (`kor_1_id`) REFERENCES `korisnik` (`id`),
  CONSTRAINT `soba_kor_2_id_6e43d84a_fk_korisnik_id` FOREIGN KEY (`kor_2_id`) REFERENCES `korisnik` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soba`
--

LOCK TABLES `soba` WRITE;
/*!40000 ALTER TABLE `soba` DISABLE KEYS */;
/*!40000 ALTER TABLE `soba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stihovi`
--

DROP TABLE IF EXISTS `stihovi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stihovi` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nivo` varchar(1) NOT NULL,
  `poznat_tekst` varchar(255) NOT NULL,
  `nepoznat_tekst` varchar(255) NOT NULL,
  `zvuk` varchar(100) NOT NULL,
  `pes_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stihovi_pes_id_e33144a5_fk_pesma_id` (`pes_id`),
  CONSTRAINT `stihovi_pes_id_e33144a5_fk_pesma_id` FOREIGN KEY (`pes_id`) REFERENCES `pesma` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=229 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stihovi`
--

LOCK TABLES `stihovi` WRITE;
/*!40000 ALTER TABLE `stihovi` DISABLE KEYS */;
INSERT INTO `stihovi` VALUES (3,'E','So it\'s gonna be forever<br>\nOr it\'s gonna go down in flames<br>\nYou can tell me when it\'s over, mm<br>\nIf the high was worth the pain<br>','Got a long list of ex-lovers','blank_space_easy.mp3',1),(4,'N','Nice to meet you, where you been?<br>\nI could show you incredible things<br>\nMagic, madness, heaven, sin<br>\nSaw you there and I thought<br>','Oh, my God, look at that face','blank_space_normal.mp3',1),(5,'H','Rose garden filled with thorns<br>\nKeep you second guessing like<br>\n\"Oh, my God, who is she?\"<br>\nI get drunk on jealousy<br>','But you\'ll come back each time you leave','blank_space_hard.mp3',1),(6,'E','Cause there we are again on that little town street<br>\nYou almost ran the red \'cause you were lookin\' over at me<br>\n','Wind in my hair, I was there','all_too_well_easy.mp3',3),(7,'N','Oh, your sweet disposition<br>\nAnd my wide-eyed gaze<br>\nWe\'re singing in the car, getting lost upstate<br>','Autumn leaves falling down like pieces into place','all_too_well_normal.mp3',3),(8,'H','Time won\'t fly, it\'s like I\'m paralyzed by it<br>\nI\'d like to be my old self again<br>\nBut I\'m still trying to find it<br>\n','After plaid shirt days and nights when you made me your own','all_too_well_hard.mp3',3),(9,'E','You got that James Dean daydream look in your eye<br>\nAnd I got that red lip classic thing that you like<br>','And when we go crashing down, we come back every time','style_easy.mp3',4),(10,'N','It\'s been a while since I have even heard from you<br>(heard from you)<br>\nAnd I should just tell you to leave \'cause I<br>','Know exactly where it leads, but I','style_normal.mp3',4),(11,'H','Midnight<br>\nYou come and pick me up, no headlights<br>\nLong drive<br>','Could end in burning flames or paradise','style_hard.mp3',4),(12,'E','We gotta get away from here<br>\nJust stop your crying<br>\nIt\'ll be alright<br>','They told me that the end is near','sign_of_the_times_easy.mp3',5),(13,'N','It\'s a sign of the times<br>\nWelcome to the final show<br>\nHope you\'re wearing your best clothes<br>','You can\'t bribe the door on your way to the sky','sign_of_the_times_normal.mp3',5),(14,'H','We don\'t talk enough<br>\nWe should open up<br>\nBefore it\'s all too much<br>','Will we ever learn','sign_of_the_times_hard.mp3',5),(15,'E','Oh, honey (ah) <br>\nI\'d walk through fire for you<br>\nJust let me adore you<br>','Like it\'s the only thing I\'ll ever do','adore_you_easy.mp3',6),(16,'N','Walk in your rainbow paradise (paradise)<br>\nStrawberry lipstick state of mind<br>','I get so lost inside your eyes','adore_you_normal.mp3',6),(17,'H','You don\'t have to say you love me<br>\nI just wanna tell you somethin\'<br>','Lately you\'ve been on my mind','adore_you_hard.mp3',6),(18,'E','So you tie up your hair and you smile like it\'s no big deal<br>\nYou can let it go<br>\nYou can throw a party full of everyone you know<br>','And not invite your family \'cause they never showed you love','matilda_easy.mp3',7),(19,'N','You were riding your bike to the sound of \"It\'s No Big Deal\"<br>\nAnd you\'re trying to lift off the ground on those old two wheels<br>','Nothing \'bout the way that you were treated\never seemed especially alarming till now','matilda_normal.mp3',7),(20,'H','Matilda, you talk of the pain like it\'s all alright<br>\nBut I know that you feel like a piece of you\'s dead insidе<br>','You showed me a power that is strong еnough','matilda_hard.mp3',7),(21,'E','You don\'t believe it<br>\nWe do this every time<br>\nSeasons change and our love went cold<br>','Feed the flame \'cause we can\'t let it go','circles_easy.mp3',8),(22,'N','I\'ll be the bad guy now<br>\nBut, no, I ain\'t too proud<br>\nI couldn\'t be there<br>\nEven when I tried<br>','You don\'t believe it','circles_normal.mp3',8),(23,'H','Maybe you don\'t understand what I\'m going through<br>\nIt\'s only me<br>\nWhat you got to lose?<br>','Make up your mind, tell me','circles_hard.mp3',8),(24,'E','I want you out of my head<br>\nI want you out of my bedroom tonight<br>\nThere\'s no way I could save you<br>','Cause I need to be saved, too','goodbyes_easy.mp3',9),(25,'N','Said you needed this heart then you got it<br>\nTurns out that it wasn\'t what you wanted<br>','And we wouldn\'t let go and we lost it','goodbyes_normal.mp3',9),(26,'H','I want you right in my life, I want you back here tonight<br>\nI\'m tryna to cut you, no knife, I wanna slice you and dice you<br>\nMy argues possessive, it got you precise<br>','Can you not turn off the TV','goodbyes_hard.mp3',9),(27,'E','You prolly think that you are better now, better now<br>\nYou only say that \'cause I\'m not around, not around<br>\nYou know I never meant to let you down, let you down<br>','Woulda gave you anythin\', woulda gave you everythin\'','better_now_easy.mp3',10),(28,'N','I did not believe that it would end, no (end, no)<br>\nEverythin\' came second to the Benzo (Benzo)<br>\nYou\'re not even speakin\' to my friends, no<br>','You knew all my uncles and my aunts though','better_now_normal.mp3',10),(29,'H','I was so broken over you (over you)<br>\nLife, it goes on, what can you do?<br>\nI just wonder what it\'s gonna take (what\'s it gonna take)<br>\nAnother foreign or a bigger chain<br>','Because no matter how my life has changed','better_now_hard.mp3',10),(30,'E','Nije ona ja<br>\nNema vatru u genima<br>\nJa nisam kriva sto je druga<br>\nI kad sve sa sebe skine<br>','I sto novom tetovazom krijes moje ime','legitimno_easy.mp3',11),(31,'N','Znate vi to oboje<br>\nSto je moje nikad nece biti njeno<br>','Zato meni uvek dobro je','legitimno_normal.mp3',11),(32,'H','Neka si je doveo<br>\nDa na moje oci glumis laznu srecu<br>','Znam te, smesta bi me poveo','legitimno_hard.mp3',11),(33,'E','Nismo bili ista liga, nista licno<br>\nZato nadji sebi nesto slicno<br>\nA ja sam odlicno, jer mi vise nije stalo<br>','A ja sam odlicno, da je bolje ne bi valjalo','ja_sam_odlicno_easy.mp3',12),(34,'N','Kazu da ti lose ide posle nase veze<br>\nDa te ovih dana rade samo tuzne pesme<br>\nKazu to, pa nisi valjda propao<br>','Ko bi rek\'o da ce tako lose da ti krene','ja_sam_odlicno_normal.mp3',12),(35,'H','Kazu da te pola nema, da si svoja sena<br>','Kad te pitaju za mene zaplaces k\'o zena','ja_sam_odlicno_hard.mp3',12),(36,'E','I volecu te ko niko nikada<br>\nSve do zadnjeg dinara<br>\nDa l\' te iko voleo toliko<br>','Znaj, ni ova igra nema kraj','psiho_easy.mp3',13),(37,'N','Ja cu da ih platim, ja cu muke da ti skratim<br>\nA da vidis kako mogu ja to<br>','Ja cu da ih kitim da ti dobro nece biti','psiho_normal.mp3',13),(38,'H','Dva dana ludilo, jos me nije ubilo<br>\nMislis da cu poslednja da saznam<br>','Dva dana previse, dobro ti se ne pise','psiho_hard.mp3',13),(39,'E','So don\'t get comfortable<br>\nLook, I don\'t dance now<br>\nI make money moves (ayy, ayy)<br>\nSay I don\'t gotta dance<br>','I make money move','bodak_yellow_easy.mp3',14),(40,'N','You know where I\'m at<br>\nYou know where I be<br>\nYou in the club just to party<br>\nI\'m there, I get paid a fee<br>','I be in and out them banks so much','bodak_yellow_normal.mp3',14),(41,'H','You a goofy, you a opp<br>\nDon\'t you come around my way<br>\nYou can\'t hang around my block<br>\nAnd I just checked my accounts<br>','Turns out, I\'m rich, I\'m rich, I\'m rich','bodak_yellow_hard.mp3',14),(42,'E','I like those Balenciagas (Those), the ones that look like socks<br>\nI like going to the jeweler, I put rocks all in my watch (Cha-ching)<br>','I like texts from my exes, when they want a second chance','i_like_it_easy.mp3',15),(43,'N','Diamond district in the jag<br>\n(Gang, I said I like it like that)<br>\nCertified, you know I\'m gang, gang<br>\n(Gang, gang I said I like it like)<br>','Drop the top and blow the brains','i_like_it_normal.mp3',15),(44,'H','Bad Bunny baby, bebé, bebé, bebé<br>\nCertified, you know I\'m gang, gang (Gang, gang I said I like it like)<br>\nDrop the top and blow the brains, wouh (Wouh! I said I like it like that)<br>','Oh he\'s so handsome, what\'s his name?','i_like_it_hard.mp3',15),(45,'E','You get a little bag and take it to the store (store, money)<br>\nGet a little cash (money)<br>\nYou shake it real fast, you get a little more (money)<br>','I got bands in the coupe','money_easy.mp3',16),(46,'N','I heard that Cardi went pop<br>\nYeah, I did go pop (pop)<br>\nThat\'s me bustin\' they bubble<br>\nI\'m Dasani with the drip<br>','Baby mommy with the clip','money_normal.mp3',16),(47,'H','Wakanda forever<br>\nSweet like a honey bun, spit like a Tommy gun<br>\nRollie a one of one, come get your mommy some<br>','Cardi at the tip-top','money_hard.mp3',16),(48,'E','Streets not safe<br>\nBut I never run away<br>\nEven when I\'m away<br>\nOT, OT, there\'s never much love when we go OT<br>','I pray to make it back in one piece','one_dance_easy.mp3',17),(49,'N','Strength and guidance<br>\nAll that I\'m wishin\' for my friends<br>\nNobody makes it from my ends<br>\nI had to bust up the silence<br>','You know you gotta stick by me','one_dance_normal.mp3',17),(50,'H','That\'s why I need a one dance<br>\nGot a Hennessy in my hand<br>\nOne more time \'fore I go<br>','Higher powers taking a hold on me','one_dance_hard.mp3',17),(51,'E','And still<br>\nBad things<br>\nIt\'s a lot of bad things<br>','That they wishin\' and wishin\' and wishin\' and wishin\'','gods_plan_easy.mp3',18),(52,'N','I feel good, sometimes I don\'t, ayy, don\'t<br>\nI finessed down Weston Road, ayy, \'nessed<br>\nMight go down a G-O-D, yeah, wait<br>','I go hard on Southside G','gods_plan_normal.mp3',18),(53,'H','She say, \"Do you love me?\" I tell her, \"Only partly<br>\nI only love my bed and my momma, I\'m sorry\"<br>','Fifty Dub, I even got it tatted on me','gods_plan_hard.mp3',18),(54,'E','You used to call me on my cell phone<br>\nLate night when you need my love<br>\nCall me on my cell phone<br>\nLate night when you need my love<br>','And I know when that hotline bling','hotline_bling_easy.mp3',19),(55,'N','Got a reputation for yourself now<br>\nEverybody knows and I feel left out<br>\nGirl you got me down, you got me stressed out<br>','Cause ever since I left the city, you','hotline_bling_normal.mp3',19),(56,'H','You don\'t need no one else<br>\nYou don\'t need nobody else, no<br>\nWhy you never alone<br>','Why you always touching road','hotline_bling_hard.mp3',19),(57,'E','In New York (ayy, ah-ha) (uh, yeah)<br>\nConcrete jungle (yeah) where dreams are made of<br>\nThere\'s nothin\' you can\'t do (yeah) (okay)<br>\nNow you\'re in New York (ah-ha, ah-ha, ah-ha) (uh, yeah)<br>','These streets will make you feel brand new','empire_state_of_mind_easy.mp3',20),(58,'N','Right next to De Niro, but I\'ll be hood forever<br>\nI\'m the new Sinatra, and since I made it here<br>\nI can make it anywhere, yeah, they love me everywhere<br>\nI used to cop in Harlem, hola, my Dominicanos <br>','Right there up on Broadway','empire_state_of_mind_normal.mp3',20),(59,'H','Lights is blinding, girls need blinders<br>\nSo they can step out of bounds quick, the sidelines is<br>\nLined with casualties, who sip the life casually<br>','Then gradually become worse, don\'t bite the apple, Eve','empire_state_of_mind_hard.mp3',20),(60,'E','The music\'s for the sad man<br>\nForever young<br>\nI wanna be forever young<br>','Do you really want to live forever?','young_forever_easy.mp3',21),(61,'N','Heaven can wait we\'re only watching the skies<br>\nHoping for the best but expecting the worst<br>\nAre you gonna drop the bomb or not?<br>','Let us die young or let us live forever','young_forever_normal.mp3',21),(62,'H','So we live a life like a video<br>\nWhen the sun is always out and you never get old<br>\nAnd the champagne\'s always cold<br>\nAnd the music is always good<br>','And the pretty girls just happened to stop by in the hood','young_forever_hard.mp3',21),(63,'E','Oh they want me to fall (fall)<br>\nFall from the top (top), They want me to drop (drop)<br>\nThey want me to stop (stop), They want me to go (go)<br>','I\'m already gone (already)','already_home_easy.mp3',22),(64,'N','Only time they excitin\' is when they mentioning Shawn<br>\nYou see single white female when she dyed her hair blonde<br>\nSometimes I look at these rappers, the movie remind me of them<br>','Somebody turn these boys off','already_home_normal.mp3',22),(65,'H','(Hey, I\'m already home) (Hey, I\'m already home)<br>\n(Hey, I\'m already home)<br>\nI\'m in the hall already, on the wall already<br>\nI\'m a work of art, I\'m a Warhol already<br>','On another level, on another plane already','already_home_hard.mp3',22),(66,'E','Don\'t call my name<br>Don\'t call my name, Alejandro<br>I\'m not your babe<br>','I\'m not your babe, Fernando','alejandro - easy.mp3',23),(67,'N','She\'s got both hands<br>In her pocket<br>And she won\'t look at you<br>Won\'t look at you','She hides true love','alejandro - normal.mp3',23),(68,'H','She\'s not broken<br>She\'s just a baby<br>But her boyfriend\'s like a dad, just like a dad','And all those flames that burned before him','alejandro - hard.mp3',23),(69,'E','I want your love, and I want your revenge<br>You and me could write a bad romance (oh-oh-oh-oh-oh)<br>I want your love and all your lover\'s revenge','You and me could write a bad romance','bad romance - easy.mp3',24),(70,'N','You know that I want you<br>And you know that I need you','I want it bad, your bad romance','bad romance - normal.mp3',24),(71,'H','I want your horror, I want your design<br>\'Cause you\'re a criminal as long as you\'re mine<br>I want your love','Love, love, love, I want your love','bad romance - hard.mp3',24),(72,'E','A ti se, blago meni, lepo vrati zeni<br>Jer oboje smo losim vinom opijeni<br>A ja cu, blago tebi, gde mi srce krene','Pa naci ce se neko pravi i za mene','blago meni - easy.mp3',25),(73,'N','Da znam da letim, ptica bih bila<br>Ovo sto grlis bila bi krila<br>Al\' ja sam zena, ne sivi soko','Plasim se kada letim visoko','blago meni - normal.mp3',25),(74,'H','Svud oko tebe mlade i lepe<br>Za svoja srca one ne strepe<br>Idi, pa lazi, govori njima','Al\' nemoj zeni sto proslost ima','blago meni - hard.mp3',25),(75,'E','Boze, Boze, kako patim<br>Kada nisi tu<br>Kao cvet bez kapi rose','Ja bez tebe uvenucu','boze boze - easy.mp3',26),(76,'N','Zima dodje sa planine<br>Hladne ruke traze te<br>Da mi dodjes, da se vratis','Bol da nestane','boze boze - normal.mp3',26),(77,'H','Sneg se topi, sve zeleni<br>Prve laste vec su tu<br>A jos uvek tebе nema','U mom narucju','boze boze - hard.mp3',26),(78,'E','But mama I\'m in love with a criminal<br>And this type of love isn\'t rational, it\'s physical<br>Mama please don\'t cry, I will be alright','All reason aside I just can\'t deny, I love that guy','criminal - easy.mp3',27),(79,'N','I know you told me I should stay away<br>I know you said he\'s just a dog astray<br>He is a bad boy with a tainted heart','And even I know this ain\'t smart','criminal - normal.mp3',27),(80,'H','He is a villain by the devil\'s law<br>He is a killer just for fun, fun, fun, fun<br>That man\'s a snitch and unpredictable','He\'s got no conscience, he got none, none, none, none','criminal - hard.mp3',27),(81,'E','A sad mi daj njen broj<br>Da \'mesto tebe ja<br>Raskinem sa njom<br>Da pozovem je<br>I kazem da si tu','I da si za mnom lud','da raskinem sa njom - easy.mp3',28),(82,'N','Uradi mi sad sve<br>Sto si s njom bez mene radio<br>Znam radio si to','Samo da bi mi se zgadio','da raskinem sa njom - normal.mp3',28),(83,'H','A sada muci me<br>Kao sto si i nju mucio<br>Znam radio si to','Samo da bi mi se smucio','da raskinem sa njom - hard.mp3',28),(84,'E','If I said my heart was beating loud<br>If we could escape the crowd somehow<br>If I said I want your body now','Would you hold it against me?','hold it against me - easy.mp3',29),(85,'N','Hey over there, please forgive me<br>If I\'m coming on too strong<br>Hate to stare, but you\'re winning','And they\'re playing my favorite song','hold it against me - normal.mp3',29),(86,'H','Give me something good<br>Don\'t wanna wait, I want it now<br>Pop it like a hood','And show me how you work it out','hold it against me - hard.mp3',29),(87,'E','Nemam ja godine<br>Nemam ime ni prezime<br>S tobom krv sam promenila','Sebe sam pobedila','ime i prezime - easy.mp3',30),(88,'N','Volela sam jednom ja i prevarena ja sam bila<br>Iz te bolesti i najjaci se ne izvuku','Od tada smejem se kad o moje srce slome ruku','ime i prezime - normal.mp3',30),(89,'H','Neka vreme prolazi, ja verovacu u trenutke<br>Kad smo zajedno, kad pogledas me iz sve snage','I vratis licu mom tu besmrtnu lepotu lutke','ime i prezime - hard.mp3',30),(90,'E','Kada bi me pitali<br>S kim bih noci nocila<br>Kada bi me pitali','S kim bih zore cekala','kada bi me pitali - easy.mp3',31),(91,'N','Hej, s tobom bih<br>Nocu zvezde brojala<br>Hej, s tobom bi','Zori rosu ukrala','kada bi me pitali - normal.mp3',31),(92,'H','Kada bi me pitali<br>Da l\' sam se zaljubila<br>Kada bi me pitali','Ja bih svima priznala','kada bi me pitali - hard.mp3',31),(93,'E','Znam da laze me, znam da vara me<br>Kralj ponoci, prosjak zore<br>Sa njim bice samo gore','Promeni ga, srce moje','kralj ponoci - easy.mp3',32),(94,'N','On je pesma moje duse<br>Kratak pljusak posle suse<br>On je pesma moje duse','Sa njim zivot nije bajk','kralj ponoci - normal.mp3',32),(95,'H','On je biser zelje moje<br>Lazni biser, crne boje<br>On je biser zelje mojе','Postelja mu moja skoljka','kralj ponoci - hard.mp3',32),(96,'E','Pao mrak, pao mrak<br>Dok te cekam zemlja puca<br>Igra se, peva se<br>To leci luda srca<br>I merak i merak','Sta ima veze sto je utorak','pao mrak - easy.mp3',33),(97,'N','Pije me ovo vino, u telu mom mu fino<br>Vec me do pola popilo<br>Jos da su oci tvoje bar pored senke moje','Svu bi me vec potopilo','pao mrak - normal.mp3',33),(98,'H','Ovaj me Mesеc gleda, san mi na oci ne da<br>Tu bih do jutra ostala<br>Jos da su usne tvojе kraj mene, zlato moje','Nikada ne bih zaspala','pao mrak - hard.mp3',33),(99,'E','Vendetta, whatever, whenever<br>Any level \'cause I can turn into a devil<br>We can hit the gas, put the pedal to the metal','I ain\'t playin\' games, all scores get settled','personal problem - easy.mp3',34),(100,'N','I\'ll be the bad guy if that makes you happy<br>Don\'t smile in my face, and no, don\'t at me<br>I mean, if you\'re broke, you\'re not in the conversation','Time is money, I don\'t get paid for my patience','personal problem - normal.mp3',34),(101,'H','Live your life, please, don\'t watch mine<br>Oh, you mad? I don\'t know why<br>That sound like a personal problem<br>That sound like a personal problem','I\'m top shelf, you way at the bottom','personal problem - hard.mp3',34),(102,'E','\'Cause my heart beats for you only<br>I wonder if you even know me<br>Countin\' down every moment','That I wait for ya, I wait for ya','savior - easy.mp3',35),(103,'N','Been around the world and I, I, I<br>I can\'t find my baby<br>Things gettin\' crazy, losin\' my patience','Why you keep me waitin\'? Goin\' through the phases','savior - normal.mp3',35),(104,'H','I feel like God playin\' tricks on me, got a fix on me<br>Feel the weight of the world like I got a brick on me<br>Had a dance with the devil and he got a grip on me','I\'m just tryna get to heaven, hope you got a ticket for me, huh','savior - hard.mp3',35),(105,'E','Starships were meant to fly<br>Hands up and touch the sky (Oh-oh-oh-oh)<br>Can\'t stop \'cause we\'re so high','Let\'s do this one more time','starships - easy.mp3',36),(106,'N','I\'m on the floor, floor, I love to dance<br>So give me more, more \'til I can\'t stand<br>Get on the floor, floor like it\'s your last chance','If you want more, more, then here I am','starships - normal.mp3',36),(107,'H','Now everybody let me hear you say, \"Ray, ray, ray\"<br>Now spend all your money, \'cause today payday<br>And if you a G, you a G-G-G','My name is Onika, you can call me Nicki','starships - hard.mp3',36),(108,'E','Tamo gde si ti, tamo stanuje mi dusa<br>Ranjena dusa zeljna ljubavi<br>Tamo gde si ti, tamo stanuje mi dusa','I sve je moje tamo gde si ti','tamo gde si ti - easy.mp3',37),(109,'N','Sta ce mi ovo jutro na pragu?<br>Zasto da zivim za novi dan?<br>Ne vidim puta i gubim nadu','Bez tebe samo za tugu znam','tamo gde si ti - normal.mp3',37),(110,'H','Zatvorim oci, vidim ti lice<br>Na hladan jastuk polozim dlan<br>Da sam te samo volela manje','Mozda bi nocas ti bio sam','tamo gde si ti - hard.mp3',37),(111,'E','Baby I got me, baby I got me<br>Yeah, that\'s all I need<br>Yeah, that\'s all I need<br>Baby I got me, only friend I need','Playing on my team is someone like','team - easy.mp3',38),(112,'N','Turn me up, break the knob right<br>I get dressed like it\'s prom night<br>I feed them lemons in the limelight','They say I\'m full, lost my appetite','team - normal.mp3',38),(113,'H','Outchea, pronto<br>Hit \'em with the dose, that\'s a combo<br>Running through ya block, no fumble','Bout to kill \'em all, where the shovel?','team - hard.mp3',38),(114,'E','With a taste of your lips, I\'m on a ride<br>You\'re toxic, I\'m slippin\' under<br>With a taste of a poison paradise<br>I\'m addicted to you','Don\'t you know that you\'re toxic?','toxic - easy.mp3',39),(115,'N','Too high, can\'t come down<br>Losing my head, spinnin\' \'round and \'round','Do you feel me now?','toxic - normal.mp3',39),(116,'H','It\'s getting late to give you up<br>I took a sip from my devil\'s cup','Slowly, it\'s taking over me','toxic - hard.mp3',39),(117,'E','Trazio si sve, sve sam ti dala<br>Tebi reci \"Ne\" nikad nisam znala<br>Citav moj si svet','Za druge necu da znam','trazio si sve - easy.mp3',40),(118,'N','Ja te volim, od ljubavi sva gorim<br>Paticu i plakacu, al\' necu da molim<br>Ja svoje srce i sve sam ti dala','A od tebe ni \"Oprosti\", ni \"Hvala\"','trazio si sve - normal.mp3',40),(119,'H','Zaklinjo si se, ljubav obecavo<br>Nadala sam se, snagu si mi davo<br>Kao nikad pre','Sanjala sam nestvarne sne','trazio si sve - hard.mp3',40),(120,'E','I-I-I wanna give you one last option<br>I-I-I wanna give you one last chance<br>If-if you looking for the main attraction','Just hold on tight, and let me do my dance','va va voom - easy.mp3',41),(121,'N','Just met a boy, just met a boy, when<br>He can come inside of my playpen<br>\'Cause he look like a superstar in the making','So, I think that I\'m going in for the takin\'','va va voom - normal.mp3',41),(122,'H','Just met a boy, just met a boy when<br>He can become my little problem<br>\'Cause it look like he modeling clothes in Dublin','So, I think he that getting that green, a goblin','va va voom - hard.mp3',41),(123,'E','Don\'t say goodbye, look in my eyes<br>So that I always will remember<br>Frozen in time, always be mine','Baby boy, you\'ll be young forever','young forever - easy.mp3',42),(124,'N','I used to think that we\'d run away<br>One lovely pretty summer day<br>I remember when you would say','We\'d be okay, come what may','young forever - normal.mp3',42),(125,'H','I used to think that we\'d reunite<br>I\'d be your wife in the real life<br>I thought that you\'d come back for me','And you would take me away','young forever - hard.mp3',42),(127,'E','Iako znam da ljubav nema pravila<br>taj osjecaj krivice imam danima<br>za grube reci sto su pale','za ruke koje nisu znale','da si tu - lakse.mp3',43),(128,'N','Proveravam telefon svoj iz navike<br>za propusteni poziv tvoj bih dao sve<br>zar nije vredna ljubav moja<br>ni poruke sa tvoga broja, zar mora','bol u crno da me zavije','da si tu - teze.mp3',43),(129,'H','Da mi je<br>Da si tu bar noci ove<br>da si tu, jedino moje<br>da si tu','da oci dusu odmore','da si tu - refren.mp3',43),(130,'E','Zivim k’o vampir, ne dam Suncu da me sretne<br>Jos jedna noc u laznom raju iza mene<br>I skupo vino','I ne tako skupe zene','oko mene sve - lakse.mp3',44),(131,'N','Bacicu cigarete ponavljam u sebi<br>Pa novu palim da zaboravio ne bih<br>Ako me secanje na tebe ne dotuce','Ja bicu sutra bolji covek nego juce','oko mene sve - teze.mp3',44),(132,'H','Oko mene sve, ceo zivot je laz<br>Dodji voli me, ti to jedina znas<br>Oko mene sve, sad me vuce na dno','Dodji spasi me ti mi dugujes to','oko mene sve - refren.mp3',44),(133,'E','Bez tebe nisam ziv al\' nesto me vuce<br>da ispratim noc daleko od kuce<br>a svaki greh me stigne','ko kazna i samo dotuce','sve ti dugujem - lakse.mp3',45),(134,'N','Neki se ljudi nikada ne promene<br>jer sreca koga hoce njega dodirne<br>i kol\'ko god sam gresan jos zivot voli me','kad ostala si samnom sve ove godine','sve ti dugujem - teze.mp3',45),(135,'H','Ja svojim morem plovim, putujem<br>sve manje dugujem sve vise ludujem<br>i ovih bora neka stid me je','nicim te ne zasluzujem','sve ti dugujem - refren.mp3',45),(136,'E','Verujem, cenjeni sude, da dobro poznajes ljude<br>vi barem imate posla jer cud je cud a sud je sud<br>Verujem, cenjena glavo, da si i ucio pravo<br>da svakom sudis posteno','jer cast je cast a vlast je vlast','ne lomite mi bagrenje - lakse.mp3',46),(137,'N','Ne lomite mi bagrenje, bez njih ce me vetrovi oduvati<br>Pustite ih, moraju mi cuvati<br>\njednu tajnu zlatnu kao dukati<br>ne lomite mi bagrenje, pod njima sam je ljubio','bosonogu i odbeglu od sna','ne lomite mi bagrenje - teze.mp3',46),(138,'H','I sve po zakonu, za to sam prvi<br>ne bi bilo ove krvi da je bilo sve po zakonu!<br>Vlast je vlast,i ja to postujem, <br>tu su paragrafi pa zagrabi','nek isto je i djavolu i djakonu','ne lomite mi bagrenje - refren.mp3',46),(139,'E','Vece se klati ko prezreli klip<br>Teska vremena, a ja tezak tip<br>Gravitacija zacas uzima svoje<br>Slab sam ja igrac za subotnje guzve<br>Al shvatam pomalo te pokretne spuzve','Neko pijan lakse zivot odrobija','ringispil - lakse.mp3',47),(140,'N','Curi od jutros od cetiri-pet<br>Resilo nebo da potopi svet','Nad gradom danima vise iste kulise','ringispil - teze.mp3',47),(141,'H','O, daj okreni <br>taj ringispil u mojoj glavi<br>To ne zna niko, <br>samo ti bez tebe','drveni konjici tuzno stoje','ringispil refren.mp3',47),(142,'E','Nikom ne pricam o tome<br>Brzo dodje taj talas i znam da cu da potonem<br>Spas mi donose cigani<br>oni imaju srce, za svakog od nas, briga njih','oni me pitaju sta da sviraju','svirajte mi jesen stize dunjo moja - lakse.mp3',48),(143,'N','Retko odlazim kuci a pisem jos redje<br>i slike su bledje i bledje<br>pa lepe potiskuju ruzne<br>Al\' nekad porucim pice i tako to krene<br>pa stignem u svatove njene','sve prave su ljubavi tuzne','svirajte mi jesen stize dunjo moja - teze.mp3',48),(144,'H','Svirajte mi \"Jesen stize dunjo moja\", al\' polako<br>da mi ne bi koja rec promakla<br>Sklon\'te case i bokale','razbio bih svet od sale','svirajte mi jesen stize dunjo moja - refren 2.mp3',48),(145,'E','Odakle si lijepa djevojko<br>Ko ti rodi oko plavetno<br>Ko ti dade kosu zlacanu<br>Ko te','stvori tako vatrenu','jugoslovenka - lakse.mp3',49),(146,'N','Odakle si lijepa djevojko<br>Gdje si rasla cvijece proljetno<br>Gdje te grije sunce slobodno','Kada pleses tako zanosno','jugoslovenka - teze.mp3',49),(147,'H','Oci su mi more Jadransko<br>Kose su mi klasje Panonsko<br>Sestra mi je dusa Slovenska','Ja sam Jugoslovenka','jugoslovenka - refren.mp3',49),(148,'E','Pa preko brda, asik planina<br>tebi na jastuk sletela<br>Pa preko neba ko ptica bela<br>pa sve','do sunca masala','sanjam - lakse.mp3',50),(149,'N','Sve do kraja sveta dalekih planeta<br>sa tobom bih isla ja<br>Prejahala polja, preplivala mora','pobegla od vremena','sanjam - teze.mp3',50),(150,'H','Sanjam, sanjam da sam s tobom<br>sanjam, rusim sve pred sobom<br>Sanjam, u hiljadu boja<br>sanjam, da sam opet zaljubljena i tvoja<br>Sanjam,','kako imam krila','sanjam - refren.mp3',50),(151,'E','O, kako uzimas mi dah, kad korake ti cujem<br>I k’o da nije noc, san me ne hvata<br>Ma, dodji ovde sam, iza zatvorenih vrata<br>O, ','kako ulivas mi strah','udji slobodno - lakse.mp3',51),(152,'N','Samo je jedna zvezda nocas pala<br>Sa neba sisla je<br>Sija tamo gde nasa ljubav spava','Do mene vodi te','udji slobodno - teze.mp3',51),(153,'H','Udji slobodno, vidi da li disem<br>Hiljadu sam ti ja zivota dala<br>Dodji, uzmi mi, jos i ovaj jedan<br>Sto','sam s\' tobom imala','udji slobodno - refren.mp3',51),(154,'E','Ti nikad neces znati ljubav dati<br>kao sto je ona ocu mom<br>dala sve sto imala je','sve da sacuva dom','kao moja mati - lakse.mp3',52),(155,'N','Ti nikad neces biti kao moja mati<br>sto je bila, ocu mom, kraljica, sluskinja','sve, al\' nikada po svom','kao moja mati - teze.mp3',52),(156,'H','Ne vjerujem ja u kipove<br>ni takve k\'o ti tipove<br>kad ti jednom','srce slome ne vjerujes nikome','kao moja mati - refren.mp3',52),(157,'E','Sada me ostavi malo samog<br>okreni glavu na drugu stranu<br>obuci kaput, otvori vrata','polako kreni ka svome stanu','produzi dalje -  lakse.mp3',53),(158,'N','Jer ja se isto smijem i placem<br>i imam dobre i lose strane','suvise pusim pomalo pijem','produzi dalje - teze.mp3',53),(159,'H','Produzi dalje, produzi dalje<br>idi od mene jer jos si dijete<br>u meni ima razocarenja','malo gorcine i puno sjete','produzi dalje - refren.mp3',53),(160,'E','Glavna lice, nalicje i lice<br>uspomene i sitnice','jarko pero rajske ptice','sacuvaj me boze njene ljubavi - lakse.mp3',54),(161,'N','Od onol\'kih zetvi osta saka razi<br>od onakve rapsodije samo sum','od riznice iskrenosti kusur lazi','sacuvaj me boze njene ljubavi - teze.mp3',54),(162,'H','Sacuvaj me, Boze, njene ljubavi<br>\nkoja zive rane soli, koja kaznjava i boli<br>\nizbavi me vjecnih sumnji i ljubomore, koje more dok ne pokore<br>\nSacuvaj me, Boze, njene ljubavi, onog ludila i strasti','sam se nikad necu spasti','sacuvaj me boze njene ljubavi - refren.mp3',54),(163,'E','Niko me nece<br>ni na ciji ne smem prag<br>gde cu sad moja ruzo','nigde nikom nisam drag','gde cu sad, moja ruzo - lakse.mp3',55),(164,'N','Gde cu sad moja ruzo<br>kad na srcu lezi trn<br>napolju mrak ko djavo','ja u dusi vise crn','gde cu sad, moja ruzo - teze.mp3',55),(165,'H','Ni na istok, ni na zapad<br>na sever, ni jug<br>nigde, nigde bez tebe se','vrtim jos u krug','gde cu sad, moja ruzo - refren.mp3',55),(166,'E','Ne znas ti kako je imati pa nemati<br>ne znas ti kako je ljubiti pa gubiti<br>ne znas ti kako je','normalan biti pa poludeti','imati pa nemati - lakse.mp3',56),(167,'N','Ne znas ti kako je kad te drze navike<br>ne znas ti kad srce broji samo oziljke<br>ne znas ti','kad se ne uzvrati ljubav kako zaboli','imati pa nemati - teze.mp3',56),(168,'H','Sad ostani jer trebas mi<br>pa makar noc jos trajalo<br>jer to je sve','sto je od nas ostalo','imati pa nemati - refren.mp3',56),(169,'E','Sta da kazem majci sto me nema<br>da se javim u dom da joj svratim<br>Sta da kazem','sta da slazem sad','nedelja - lakse.mp3',57),(170,'N','Sta da kazem ocu<br>kad me pita gde sam, s kim sam','kako sam sta radim','nedelja - teze.mp3',57),(171,'H','Nedelja, i svi ste tu<br>sve podseca na srecu<br>nedelja, a vise','vas ja zagrliti necu','nedelja - refren.mp3',57),(172,'E','Ni okrenuo se nisi, zamnom kao drugi svijet<br>niti gurnuo kamencic, zamnom jednom zauvijek<br>A ja samo sam, htjela oca djeci<br>Malo ljubavi','pa ti sada reci','bizuterija - lakse.mp3',58),(173,'N','Ti si nadaren ko niko<br>skolovani prevarant<br>imao si nisi znao','kako sjaji dijamant','bizuterija - teze.mp3',58),(174,'H','A bila sam ti sudjena<br>blago meni, jos po sebi, tvoje prste osjecam<br>Ja sam ti bila privjezak<br>sto se sija, obmana il\' kopija<br>sto se nosi','da se vidi ko je jak','bizuterija - refren.mp3',58),(175,'E','Ja te sretnoga sanjam na dane, pa mi kapa samoca na rame<br>kako samo mi nedostajes, ni ne pitas se da l\' smijes<br>Ko led u kosti ljubav se uvukla<br>zelja','za tobom skroz me dotukla','kad bi bio blizu - lakse.mp3',59),(176,'N','Ja se osjecam lose na dane<br>ko bi sa mnom zamjenio strane<br>moja vojska suza ranjena','jos se nije povukla','kad bi bio blizu - teze.mp3',59),(177,'H','Kad bi bio blizu<br>bio blizu kraj mene<br>jednu noc bez suza','dugujes mi najmanje','kad bi bio blizu - refren.mp3',59),(178,'E','Ne priznaj nikome da ides kod mene<br>preskoci pitanja i sve stepenice<br>kad vidim te za srce zalijepi se med','jer jedanaesta za mene ti si zapovjed','minus i plus - lakse.mp3',60),(179,'N','Jesi li blizu il\' me vara osjecaj<br>cujem li tebe ili srca otkucaj<br>u ovoj prici sve me navodi na grijeh<br>zivot mi','vec odavno nema raspored','minus i plus - teze.mp3',60),(180,'H','Trebam te ja, nije nacin da<br>okreces mi ledja zato jer smo razlika<br>ko minus i plus, ko Amer i Rus<br>u mom svijetu','ti si korov a ja hibiskus','minus i plus - refren.mp3',60),(181,'E','Jednom kad se vratis<br>Sve ce biti deo proslosti','Sve osim moje ljubavi','idu dani - lakse.mp3',61),(182,'N','Al\' je bilo boli<br>U tim lepim, tamnim ocima','Sto jos ih sanjam noc i dan','idu dani - teze.mp3',61),(183,'H','Ja cekacu te do sitnog sata<br>I nosicu tvoj dar oko vrata<br>Da opet vidim tvoje lice','Mala bela gospodjice','idu dani - refren 2.mp3',61),(184,'E','Cekao sam, draga, ovu noc sve ove godine<br>Cuvao sam reci samo da ti kazem \"ne\"<br>Ti potrosila si sve dobre prilike<br>Sad se vracas meni, zato bolje kreni<br>Jer i ja sam potrosen, racun ugasen','I tu staru tebe ne zasluzujem','michelle - lakse.mp3',62),(185,'N','Znam ti pravu stranu, svaku tvoju manu dobro znam<br>Za te price tvoje pretesan je ovaj mali stan','Pa obuci kaput svoj','michelle - teze.mp3',62),(186,'H','Michelle (Michelle)<br>Nisi vise lepa kao pre (Michelle)<br>Moj te pogled ne prepoznaje','Ne zovi suze u pomoc','michelle - refren.mp3',62),(187,'E','Mirise ti kosa, jos taj miris osecam<br>Ne, ne mozes uci, ja ne zivim vise sam<br>Da l\' on te voli, znaj, jos me boli','Poslednji zagrljaj kada si otisla','zaboravljas - lakse.mp3',63),(188,'N','Nocas bez glasa ti na mojim vratima<br>Na licu ti kisa znam da lije satima','I neka lije bar suze krije','zaboravljas - teze.mp3',63),(189,'H','Zaboravljas<br>Sta smo jednom davno rekli<br>Kad ostavljas, ostavljas<br>Sve sto smo stekli<br>Sacuvaj bar, onaj ponos','U tvom glasu koji sam voleo','zaboravljas - refren.mp3',63),(190,'E','Nocas moje molbe nebo ne cuje<br>dusa mi je prazna k\'o da umire<br>nocas drugi spava na tvom ramenu<br>a na mome','dlanu zvezde umiru','ako odes - lakse.mp3',64),(191,'N','Reci koga ljubis, koga opijas<br>kome zivot nudis usnama od otrova<br>prokleto ti bilo sto si lagala','zivot sam ti dao, sve si uzela','ako odes - teze.mp3',64),(192,'H','Mislio sam, ako odes<br>da ce manje biti boli<br>al\' uzalud, sto si dalje','tebe srce vise voli','ako odes - refren.mp3',64),(193,'E','Jos jedan gradski pastuh je<br>u nocnu trku krenuo<br>i da se rodi ponovo','\ntaj ne bi se promenio','bezobrazno zelene - lakse.mp3',65),(194,'N','Jos jedan gradski kauboj<br>u nocni pohod krece svoj<br>on dane nocu provodi<br>i zene u mrak odvodi<br>A onda sam te video','u glavu krv se sjurila','bezobrazno zelene - teze.mp3',65),(195,'H','Bezobrazno su zelene<br>te tvoje oci nevine<br>pa hoce da me promene<br>da mi se zivot okrene<br>Bezobrazno su zelene','pa rade svasta od mene','bezobrazno zelene - refren.mp3',65),(196,'E','Nije tebi nocas mesto u mom hladnom hodniku<br>da bi dosla do mog srca ne znas tajnu lozinku<br>Tebi treba neko snazan, neko jak i siguran','a ne covek kao ja','grlica - lakse.mp3',66),(197,'N','Sto si to u meni nasla<br>moja tuzna grlice<br>sto su drumovi za mene','za tebe su ulice','grlica - teze.mp3',66),(198,'H','Za jednu noc kraj mene<br>ti bi dala ceo svet<br>a ja sve sve sto imam<br>za tvojih dvadeset i pet<br>Za jednu noc kraj mene','ti bi srusila svoj let','grlica - refren.mp3',66),(199,'E','Jer vidim ja kroz tebe sve<br>Ti zelis me, a druge ne<br>Na tebi je bas sve naj, naj<br>Sto','posto znam da ti si taj','bradd pitt - lakse.mp3',67),(200,'N','Ispred mene DJ, iza rusi se sve<br>Oko mene su svi ludi, samo ne ti<br>Novi vrti se hit, a ti kao Bred Pit<br>Od sto pedeset, njih sto','s tobom bi radile to','bradd pitt - teze.mp3',67),(201,'H','Ovo ce biti dobra noc, predosjecam<br>Tvoje su oci boje ranog proljeca','Nocni klub i svi smo tu','bradd pitt - refren.mp3',67),(202,'E','Samo smo se smijali i pricali o genima<br>Mastali o djeci,i o njihovim imenima, mislili da skupa cemo zlo i dobro dijeliti<br>Za bolji zivot stedjeti u bolji kraj preseliti, ali tebi ocigledno sve to bilo malo<br>Jer zbog tvoje glupe slabosti, sve u','Jedna ruzna rijec dobro te opisuje','dobrodosao u klub - lakse.mp3',68),(203,'N','Vjerovala sam u tvoju pricu da si pravi<br>Da jedina sam ja u tvome srcu,u tvojoj glavi<br>A ti bio si dno, varao me sa sto','Sada gledaj me i pati','dobrodosao u klub - teze.mp3',68),(204,'H','Dobrodosao u klub<br>Sjedi udobno se smjesti<br>Prevarenih ima svud<br>Zar to nisu dobre vijesti?<br>Mene ti,a tebe ja','Ama svima to se desi','dobrodosao u klub - refren.mp3',68),(205,'E','Znam umire ljubav<br>Tisina sve mi govori<br>o pobjedi i porazu<br>Ti','samo si u prolazu','grad bez ljudi - lakse.mp3',69),(206,'N','Komad po komad<br>Moje srce kruni se<br>A ja sam tu da cekam te','I da za slamku drzim se','grad bez ljudi - teze.mp3',69),(207,'H','Vidjela sam grad bez ljudi<br>Pobjednika kako gubi<br>Andjele na stupu srama<br>Djecu koja placu sama','Vidjela sam snijeg u maju','grad bez ljudi - refren.mp3',69),(208,'E','Ah<br> sto cemo ljubav kriti','kad ja moram tvoja biti','a sto cemo ljubav kriti - lakse.mp3',70),(209,'N','Il\' me uzmi<br>il\' me ubi','ne daj drugom da me ljubi','a sto cemo ljubav kriti - teze.mp3',70),(210,'H','Srce<br>vise nije moje','tebi dragi pripalo je','a sto cemo ljubav kriti - refren.mp3',70),(211,'E','Ciganine, sviraj, sviraj<br>pesmom moju dusu diraj<br>nek\' mi tvoja pesma kaze','kad\' me ljubi sto me laze','ciganine, sviraj, sviraj - lakse.mp3',71),(212,'N','Nekada smo sretni bili<br>nasu ljubav nismo krili<br>mislila sam, dani srece','da nikada proci nece','ciganine, sviraj, sviraj - teze.mp3',71),(213,'H','da li znas za moje boli<br>sad moj dragi drugu voli<br>Nekad sam bila ja<br>srecna i voljena<br>dok druga zena','nije moju ljubav uzela','ciganine, sviraj, sviraj - refren.mp3',71),(214,'E','Moje je lice bledo, majko<br>jer on mi zivot uze<br>necu ga, necu, kleti majko','proste mu moje suze','rane moje - lakse.mp3',72),(215,'N','Sve mi je pusto bez njega, majko<br>duga je, duga noc<br>srce se steze a dusa boli<br>kada','pomislim da ce mi od nje doc\'','rane moje - teze.mp3',72),(216,'H','Rane, rane moje, teske rane<br>kako da prebolim<br>kako da ga kunem, majko<br>kad ga moja dusa hoce','kad ga moje srce zeli','rane moje - refren.mp3',72),(217,'E','Pesme moje, pesme moje<br>ni za sta me ne krivite<br>ostanite s\' drugovima','i za mene zivite','pesme moje - lakse.mp3',73),(218,'N','Dao sam vam dusu svoju<br>dao sam vam dane mladosti<br>delio sam zivot s\' vama','svoje tuge svoje radosti','pesme moje - teze.mp3',73),(219,'H','O Danka, Danka, Danka, o Marija<br>hej Branka, Branka, Branka<br>prokleta je ova nedelja<br>o majko sto me rodi<br>kad srece nemam ja','dotako sam dno zivota','pesme moje -refren.mp3',73),(220,'E','Sta ce mi zivot kad je nema majko<br>Jer drugu ljubav ne zelim da imam<br>Sanjam je, sanjam skoro svake noci','Ona je tu u srcu mom','sta ce mi zivot - lakse.mp3',74),(221,'N','Jesen je tuzna vec odavno dosla<br>Uzalud cekam, uzalud se nadam<br>O','majko moja koliko je volim','sta ce mi zivot - teze.mp3',74),(222,'H','Nocas mi srce pati<br>Nocas me dusa boli<br>Tesko je kad se voli','Kad ostanes sam','sta ce mi zivot - refren.mp3',74),(223,'E','Svirajte mi vi, tiho, tiho<br>svirajte mi vi, tiho, tise<br>tiho, tiho','svirajte mi vi nema nje','svirajte mi tiho tise - lakse.mp3',75),(224,'N','Ovu noc<br> tiho, tiho<br>ovu','noc tiho tise','svirajte mi tiho tise - teze.mp3',75),(225,'H','Nema nje, nema nje<br>pustite me, pustite me','da bolim svoju bol','svirajte mi tiho tise - refren.mp3',75),(226,'E','Ne pevajte pesme njene<br>ne dirajte staru ranu<br>pet godina ja negujem<br>pet godina ja jos cuvam','jednu ruzu za Ljiljanu','za ljiljanu - lakse.mp3',76),(227,'N','Ostvaricu snove svoje<br>kada hladne kise stanu','Kad s prolecem ozelene','za ljiljanu - teze.mp3',76),(228,'H','Ljubavi su mnoge bile<br>kao vatra mladost planu<br>sve sto osta od zivota','ja bi dao za Ljiljanu','za ljiljanu - refren.mp3',76);
/*!40000 ALTER TABLE `stihovi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zanr`
--

DROP TABLE IF EXISTS `zanr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zanr` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `naziv` varchar(31) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zanr`
--

LOCK TABLES `zanr` WRITE;
/*!40000 ALTER TABLE `zanr` DISABLE KEYS */;
INSERT INTO `zanr` VALUES (1,'Pop Strani'),(2,'Pop Domaci'),(3,'Folk'),(4,'Narodna'),(5,'Rep');
/*!40000 ALTER TABLE `zanr` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-25 17:17:06
