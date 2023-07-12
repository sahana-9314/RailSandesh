-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 05, 2023 at 02:18 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `railway`
--

-- --------------------------------------------------------

--
-- Table structure for table `passengers`
--

DROP TABLE IF EXISTS `passengers`;
CREATE TABLE IF NOT EXISTS `passengers` (
  `pnr_number` int NOT NULL,
  `train_no` int NOT NULL,
  `train_name` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `boarding` varchar(30) NOT NULL,
  `reservedupto` varchar(30) NOT NULL,
  `class` varchar(10) NOT NULL,
  `CurrStat` varchar(30) NOT NULL,
  `ChartStatus` varchar(30) NOT NULL,
  `CoachPoisition` varchar(10) NOT NULL,
  PRIMARY KEY (`pnr_number`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `passengers`
--

INSERT INTO `passengers` (`pnr_number`, `train_no`, `train_name`, `date`, `boarding`, `reservedupto`, `class`, `CurrStat`, `ChartStatus`, `CoachPoisition`) VALUES
(1234567890, 7388, 'PVR BGM UR SPL', '2023-05-30', 'PVR', 'BGM', 'SL', 'CONFIRM', 'NOT PREPARED', 'NA'),
(1231231234, 17416, 'HARIPRIYA EXP', '2023-06-05', 'KOP', 'TPTY', '1A', 'RAC', 'NOT PREPARED', 'NA'),
(1357924680, 16589, 'RANI CHENNAMMA', '2023-05-22', 'SBC', 'MRJ', '2A', 'WAITING LIST', 'NOT PREPARED', 'NA');

-- --------------------------------------------------------

--
-- Table structure for table `rbg1`
--

DROP TABLE IF EXISTS `rbg1`;
CREATE TABLE IF NOT EXISTS `rbg1` (
  `Train_Number` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Train_Name` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Source Station` varchar(14) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Desti Station` varchar(13) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Arrival` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Depart.` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Running_Days` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rbg1`
--

INSERT INTO `rbg1` (`Train_Number`, `Train_Name`, `Source Station`, `Desti Station`, `Arrival`, `Depart.`, `Running_Days`) VALUES
('7388', 'PVR BGM UR SPL', 'PVR', 'BGM', '00:35:00', '00:36:00', 'Y'),
('17318', 'DR HUBBALLI EXP', 'DR', 'UBL', '06:34:00', '06:35:00', 'Y'),
('17331', 'MRJ UBL EXP', 'MRJ', 'UBL', '07:19:00', '07:20:00', 'Y'),
('7352', 'LD MRJ EXP SPL', 'LD', 'MRJ', '09:36:00', '09:37:00', 'Y'),
('7335', 'BGM SED EXP SPL', 'BGM', 'SED', '09:40:00', '09:41:00', 'Y'),
('16589', 'RANI CHENNAMMA', 'SBC', 'MRJ', '10:30:00', '10:31:00', 'Y'),
('7336', 'SED BGM EXP SPL', 'SED', 'BGM', '12:41:00', '12:42:00', 'Y'),
('17333', 'MRJ CLR EXPRESS', 'MRJ', 'CLR', '12:55:00', '12:56:00', 'Y'),
('17415', 'HARIPRIYA EXP', 'TPTY', 'KOP', '12:57:00', '12:58:00', 'Y'),
('17416', 'HARIPRIYA EXP', 'KOP', 'TPTY', '14:05:00', '14:06:00', 'Y'),
('16590', 'RANICHENNAMA EX', 'MRJ', 'SBC', '16:29:00', '16:30:00', 'Y'),
('17332', 'UBL MRJ EXP', 'UBL', 'MRJ', '16:47:00', '16:48:00', 'Y'),
('17317', 'UBL DR EXPRESS', 'UBL', 'DR', '19:33:00', '19:34:00', 'Y'),
('7351', 'MRJ LD EXP SPL', 'MRJ', 'LD', '20:19:00', '20:20:00', 'Y'),
('12779', 'GOA EXPRESS', 'VSG', 'NZM', '21:01:00', '21:02:00', 'Y'),
('17334', 'CLR MRJ PASS', 'CLR', 'MRJ', '22:30:00', '22:31:00', 'Y'),
('12780', 'GOA EXPRESS', 'NZM', 'VSG', '23:29:00', '23:30:00', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `trains`
--

DROP TABLE IF EXISTS `trains`;
CREATE TABLE IF NOT EXISTS `trains` (
  `train_no` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `source` varchar(50) NOT NULL,
  `destination` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `seats_available` int NOT NULL,
  PRIMARY KEY (`train_no`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `trains`
--

INSERT INTO `trains` (`train_no`, `name`, `source`, `destination`, `date`, `seats_available`) VALUES
(7388, 'PVR BGM UR SPL', 'PVR', 'BGM', '2023-05-24', 98),
(17318, 'DR HUBBALLI EXP', 'DR', 'UBL', '2023-05-24', 0),
(17331, 'MRJ UBL EXP', 'MRJ', 'UBL', '2023-05-24', 100),
(7352, 'LD MRJ EXP SPL', 'LD', 'MRJ', '2023-05-24', 100),
(7335, 'BGM SED EXP SPL', 'BGM', 'SED', '2023-05-24', 100),
(16589, 'RANI CHENNAMMA', 'SBC', 'MRJ', '2023-05-24', 100),
(7336, 'SED BGM EXP SPL', 'SED', 'BGM', '2023-05-24', 0),
(17333, 'MRJ CLR EXPRESS', 'MRJ', 'CLR', '2023-05-24', 0),
(17415, 'HARIPRIYA EXP', 'TPTY', 'KOP', '2023-05-24', 0),
(17416, 'HARIPRIYA EXP', 'KOP', 'TPTY', '2023-05-24', 100),
(16590, 'RANICHENNAMA EX', 'MRJ', 'SBC', '2023-05-24', 100),
(17332, 'UBL MRJ EXP', 'UBL', 'MRJ', '2023-05-24', 100),
(17317, 'UBL DR EXPRESS', 'UBL', 'DR', '2023-05-24', 100),
(7351, 'MRJ LD EXP SPL', 'MRJ', 'LD', '2023-05-24', 90),
(12779, 'GOA EXPRESS', 'VSG', 'NZM', '2023-05-24', 0),
(17334, 'CLR MRJ PASS', 'CLR', 'MRJ', '2023-05-24', 0),
(12780, 'GOA EXPRESS', 'NZM', 'VSG', '2023-05-24', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
