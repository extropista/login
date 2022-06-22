CREATE DATABASE IF NOT EXISTS fundacionayuda DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE fundacionayuda;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fundacionayuda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE IF NOT EXISTS  user (
  id smallint UNSIGNED NOT NULL,
  `username` varchar(20) COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` char(102) COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `fullname` varchar(50) COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Stores the user''s data.';



CREATE TABLE IF NOT EXISTS mandato (
	id int NOT NULL AUTO_INCREMENT,
    email varchar(100) NOT NULL,
    direccion varchar(100) NOT NULL,
    region varchar(100) NOT NULL,
    comuna varchar(100) NOT NULL,
    postalcode varchar(100) NOT NULL,
    PRIMARY KEY (ID)
)    ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'OGARCIA', 'pbkdf2:sha256:260000$fiRyeVmApEki8uvm$40d93cdea3f941010f3eedfafd228db15c41810ce625a691ff8cb2491300b010', 'Oscar Garcia');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
