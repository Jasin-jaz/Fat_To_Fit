/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.2.0 : Database - fat_to_fit
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fat_to_fit` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `fat_to_fit`;

/*Table structure for table `alloc_gym_ins` */

DROP TABLE IF EXISTS `alloc_gym_ins`;

CREATE TABLE `alloc_gym_ins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) DEFAULT NULL,
  `gym_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `alloc_gym_ins` */

insert  into `alloc_gym_ins`(`id`,`user_id`,`gym_id`) values 
(10,'30','22'),
(11,'25','23');

/*Table structure for table `attendence` */

DROP TABLE IF EXISTS `attendence`;

CREATE TABLE `attendence` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `batch` varchar(100) DEFAULT NULL,
  `attendence` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

insert  into `attendence`(`id`,`username`,`date`,`time`,`batch`,`attendence`) values 
(7,'vyshnav','2024-01-16','15:49:04','11','PRESENT'),
(8,'Adhith','2024-01-17','13:47:22','7','PRESENT'),
(9,'Adhith','2024-01-19','09:46 PM','7','PRESENT');

/*Table structure for table `batch` */

DROP TABLE IF EXISTS `batch`;

CREATE TABLE `batch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `batch` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `batch` */

insert  into `batch`(`id`,`batch`,`time`) values 
(6,'MORNING','5:30'),
(7,'MORNING','5:30'),
(11,'EVENING','5.00pm'),
(12,'MORNING','06:30');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `COMPLAINT_ID` int NOT NULL AUTO_INCREMENT,
  `SENDER_ID` int DEFAULT NULL,
  `COMPLAINTS` varchar(10000) DEFAULT NULL,
  `DATE` varchar(100) DEFAULT NULL,
  `REPLY` varchar(100) DEFAULT NULL,
  `REPLY_DATE` varchar(100) DEFAULT NULL,
  `TYPE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`COMPLAINT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`COMPLAINT_ID`,`SENDER_ID`,`COMPLAINTS`,`DATE`,`REPLY`,`REPLY_DATE`,`TYPE`) values 
(13,30,'complaints.....!!!!','2024-01-17','pending','pending',' USER'),
(14,23,'Replacement of requirement.','2024-01-17','pending','pending',' GYM INSTRUCTOR'),
(15,28,'complaints','2024-01-17','ok','2024-01-17','PHYSICIAN');

/*Table structure for table `completion` */

DROP TABLE IF EXISTS `completion`;

CREATE TABLE `completion` (
  `CID` int NOT NULL AUTO_INCREMENT,
  `ALLOCID` varchar(100) DEFAULT NULL,
  `STARTING_DATE` varchar(100) DEFAULT NULL,
  `ENDING_DATE` varchar(100) DEFAULT NULL,
  `STATUS` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `completion` */

insert  into `completion`(`CID`,`ALLOCID`,`STARTING_DATE`,`ENDING_DATE`,`STATUS`) values 
(7,'11','2024-01-17','0000-00-00','pending');

/*Table structure for table `diet_details` */

DROP TABLE IF EXISTS `diet_details`;

CREATE TABLE `diet_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `batch` varchar(100) DEFAULT NULL,
  `name` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `start` varchar(100) DEFAULT NULL,
  `end` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `diet_details` */

insert  into `diet_details`(`id`,`batch`,`name`,`details`,`start`,`end`,`status`) values 
(9,'7','Adhith','plans.......','2024-01-19','2024-01-27','completed');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` varchar(100) DEFAULT NULL,
  `USERNAME` varchar(100) DEFAULT NULL,
  `DATE` varchar(100) DEFAULT NULL,
  `DETAILS` varchar(100) DEFAULT NULL,
  `REPLY` varchar(100) DEFAULT NULL,
  `REPLY_DATE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`id`,`uid`,`USERNAME`,`DATE`,`DETAILS`,`REPLY`,`REPLY_DATE`) values 
(3,'25','adith@mail.com','2024-01-16','doubts!\r\n','reply for doubts...!','2024-01-17'),
(4,'30','vyshnav@mail.com','2024-01-17','doubts!!!!','doubts! reply','2024-01-17'),
(5,'30','vyshnav@mail.com','2024-01-17','one more doubts!','pending','pending');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values 
(3,25,'feedback....!','2024-01-16');

/*Table structure for table `gym_instructor` */

DROP TABLE IF EXISTS `gym_instructor`;

CREATE TABLE `gym_instructor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `housename` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(250) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `gym_instructor` */

insert  into `gym_instructor`(`id`,`name`,`housename`,`place`,`post`,`pin`,`phone`,`pic`,`email`) values 
(22,'mrdl','madhurima','kannur','kannur','670643','08745956533','/static/image/20240114-002646.jpg','mrdl@gmail.com'),
(23,'Jasin','kannur','kannur','kannur','670643','09633986989','/static/image/20240114-102754.jpg','jasintp@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `utype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`utype`) values 
(0,'admin','admin','admin'),
(22,'mrdl@gmail.com','8788','gym instructor'),
(23,'jasintp@gmail.com','9622','gym instructor'),
(25,'adith@mail.com','2233','user'),
(28,'sandesh@gmail.com','7374','physician'),
(30,'vyshnav@mail.com','1234','user');

/*Table structure for table `measures` */

DROP TABLE IF EXISTS `measures`;

CREATE TABLE `measures` (
  `measure_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `height` float NOT NULL,
  `weight` float NOT NULL,
  `bmi` float NOT NULL,
  `measure_date` date DEFAULT NULL,
  PRIMARY KEY (`measure_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `measures` */

insert  into `measures`(`measure_id`,`user_id`,`height`,`weight`,`bmi`,`measure_date`) values 
(4,25,170,75,25.9516,'2024-01-19'),
(5,25,170,70,24.2215,'2024-01-21'),
(6,30,170,65,22.4914,'2024-01-18'),
(7,30,170,65,22.4914,'2024-01-23'),
(8,30,168,67,23.7387,'2024-01-20');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `mid` int NOT NULL AUTO_INCREMENT,
  `MEDICINE_NAME` varchar(100) DEFAULT NULL,
  `MEDICINE_DETAILS` varchar(500) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `MEDICINE_PRICE` float DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `medicine` */

insert  into `medicine`(`mid`,`MEDICINE_NAME`,`MEDICINE_DETAILS`,`MEDICINE_PRICE`) values 
(3,'DFO GEL','DFO 4X Gel is used to relieve pain and reduce swelling in your joints and muscles.',200),
(4,'Hydroxycut gummies','Hydroxy cut gummies are a type of weight loss supplement that claim to help you lose weight by boost',1500),
(6,'PENTASURE 2.0','PENTASURE 2.0 is a High Protein High Calorie formula for lean weight gain. Highly recommended for dietery management for people with increased protein and energy needs.',2500);

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `medid` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`id`,`medid`,`user_id`,`quantity`,`amount`,`status`) values 
(24,4,30,4,6000,'ordered'),
(26,6,30,2,5000,'booked'),
(27,6,30,4,10000,'booked'),
(28,4,25,1,1500,'ordered');

/*Table structure for table `physician` */

DROP TABLE IF EXISTS `physician`;

CREATE TABLE `physician` (
  `id` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `housename` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `physician` */

insert  into `physician`(`id`,`name`,`housename`,`place`,`post`,`pin`,`phone`,`pic`,`email`) values 
(28,'Sandesh','Vadakkan house','Alakkode','udayagiri','674231','9992255369','/static/image/20240116-053016.jpg','sandesh@gmail.com');

/*Table structure for table `requirements` */

DROP TABLE IF EXISTS `requirements`;

CREATE TABLE `requirements` (
  `req_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `amount` float NOT NULL,
  `buy_date` varchar(100) NOT NULL,
  PRIMARY KEY (`req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `requirements` */

insert  into `requirements`(`req_id`,`name`,`pic`,`description`,`amount`,`buy_date`) values 
(12,'Treadmill','/static/image/Treadmill.jpg','Treadmill helps in reducing weight and is loved by people all across the world for its simplicity and interesting way of running indoors.',13000,'2024-01-19'),
(13,'Dumbbells','/static/image/Dumbbells.jpg','Dumbbells can be used for joint-isolation exercises such as biceps curls, chest flyes or shoulder raises',5000,'2024-01-20');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(10) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `batch_id` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`hname`,`place`,`post`,`pin`,`phone`,`pic`,`email`,`batch_id`) values 
(25,'Adhith','chintech','kannur','kannur','670014','83653652732','/static/image/20240117-145545.jpg','adith@mail.com',7),
(30,'vyshnav','rose villa','kannur','kannur','670014','7654345643','/static/image/20240117-145600.jpg','vyshnav@mail.com',11);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
