# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RN2h4(RPackage):
	"""Handling Methods for Naver News Text Crawling

	Provides some functions to get Korean text sample from news articles in
             Naver which is popular news portal service <https://news.naver.com/> in Korea.
	"""
	
	homepage = "https://github.com/forkonlp/N2H4"
	cran = "N2H4" 

	version("0.8.2", md5="a02f78c3300f32ede70b3a3decb7c689", url="https://cran.r-project.org/src/contrib/N2H4_0.8.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
