-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2021 at 06:46 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `adventure_agency`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

CREATE TABLE `user_information` (
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `age` varchar(10) NOT NULL,
  `gender` varchar(25) NOT NULL,
  `city` varchar(50) NOT NULL,
  `address` varchar(70) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`first_name`, `last_name`, `age`, `gender`, `city`, `address`, `user_name`, `password`) VALUES
('Drashti', 'Shah', '18', 'Female', 'Mumbai', 'A/1301 Parwana', 'dshah', '1234'),
('khushi', 'shah', '17', 'Female', 'Mumbai', 'Reis Magos', 'kshah', '1111'),
('Foram', 'Gandhi', '19', 'Female', 'Pune', 'Veer Tower', 'foramg', '2222'),
('drashti', 'pansaniya', '18', 'Female', 'Banglore', 'sony tower', 'dpansaniya', '2222'),
('hetvi', 'shah', '19', 'Female', 'Delhi', 'Heena Elegance', 'hshah', '9999');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
