# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRblt(RPackage):
	"""Bio-Logging Toolbox

	An R-shiny application to plot datalogger time series at a microsecond precision as Acceleration, Temperature, 
  Pressure, Light intensity from CATS, AXY-TREK LUL and WACU bio-loggers. It is possible to link behavioral labels extracted
  from 'BORIS' software <http://www.boris.unito.it> or manually written in a csv file.
  CATS bio-logger are manufactured by <https://cats.is/>, AXY-TREK are manufactured by <https://www.technosmart.eu> and 
  LUL and WACU are manufactured by <https://www.iphc.cnrs.fr/-MIBE-.html>.
	"""
	
	homepage = "https://github.com/sg4r/rblt"
	cran = "rblt"

	version("0.2.4.6", md5="b76f47938742399f509217d50f4fccff")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-hdf5r@1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("hdf5@1.8.12:", type=("build", "link", "run"))
