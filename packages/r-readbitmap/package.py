# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadbitmap(RPackage):
	"""Simple Unified Interface to Read Bitmap Images (BMP,JPEG,PNG,TIFF).

	Identifies and reads Windows BMP, JPEG, PNG, and TIFF format bitmap images.
	Identification defaults to the use of the magic number embedded in the file
	rather than the file extension. Reading of JPEG and PNG image depends on
	libjpg and libpng libraries. See file INSTALL for details if necessary."""

	cran = "readbitmap"

	version("0.1.5", md5="9221be6ab4d68a1fe9292ae60d953d32")

	depends_on("r-bmp", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
