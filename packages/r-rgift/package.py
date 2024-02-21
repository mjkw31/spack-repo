# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgift(RPackage):
	"""Create Quizzes in GIFT Format

	Implementation of some functions to create quizzes
  in the GIFT format. This format is used by several Virtual Learning
  Environments such as Moodle.
	"""
	
	homepage = "https://docs.moodle.org/21/en/GIFT_format"
	cran = "RGIFT" 

	version("0.1-6", md5="1ae4303bbd8b139fbf887ecd0ade530e")

	depends_on("r@2.10:", type=("build", "run"))
