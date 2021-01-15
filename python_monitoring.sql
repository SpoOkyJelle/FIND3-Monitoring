-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Gegenereerd op: 15 jan 2021 om 10:54
-- Serverversie: 5.7.31
-- PHP-versie: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_monitoring`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `raspberries`
--

DROP TABLE IF EXISTS `raspberries`;
CREATE TABLE IF NOT EXISTS `raspberries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `ip_adress` varchar(255) NOT NULL,
  `ram` varchar(255) NOT NULL,
  `cpu` varchar(255) NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `raspberries`
--

INSERT INTO `raspberries` (`id`, `name`, `ip_adress`, `ram`, `cpu`, `last_updated`) VALUES
(1, 'raspberry1', '167.58.25.33', '12/16', '35%', '2021-01-13 16:28:58.264000'),
(2, 'raspberry2', '6.89.134.51', '2/4', '12%', '2021-01-12 06:26:58.000000'),
(3, 'raspberry3', '193.204.83.113', '12/12', '19%', '2021-01-02 19:32:20.000000');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
