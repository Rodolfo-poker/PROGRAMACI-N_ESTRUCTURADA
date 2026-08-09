-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 09-08-2026 a las 02:58:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_diccionario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diccionario_en`
--

CREATE TABLE `diccionario_en` (
  `id` int(11) NOT NULL,
  `palabra` varchar(100) NOT NULL,
  `traduccion` varchar(100) NOT NULL,
  `significado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diccionario_en`
--

INSERT INTO `diccionario_en` (`id`, `palabra`, `traduccion`, `significado`) VALUES
(1, 'SI', 'YES', 'AFIRMACIÓN');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diccionario_fr`
--

CREATE TABLE `diccionario_fr` (
  `id` int(11) NOT NULL,
  `palabra` varchar(100) NOT NULL,
  `traduccion` varchar(100) NOT NULL,
  `significado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `diccionario_en`
--
ALTER TABLE `diccionario_en`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `diccionario_fr`
--
ALTER TABLE `diccionario_fr`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `diccionario_en`
--
ALTER TABLE `diccionario_en`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `diccionario_fr`
--
ALTER TABLE `diccionario_fr`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
