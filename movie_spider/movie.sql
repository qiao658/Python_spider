/*
Navicat MySQL Data Transfer

Source Server         : mysql57
Source Server Version : 50726
Source Host           : localhost:3306
Source Database       : account

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `mname` varchar(100) NOT NULL,
  `mdesc` text,
  `mimg` varchar(120) NOT NULL,
  `mlink` varchar(200) NOT NULL,
  PRIMARY KEY (`mid`),
  UNIQUE KEY `mname` (`mname`)
) ENGINE=InnoDB AUTO_INCREMENT=2004 DEFAULT CHARSET=utf8;
