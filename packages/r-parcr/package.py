# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParcr(RPackage):
	"""Construct Parsers for Structured Text Files

	Construct parser combinator functions, higher order functions that
  parse input. Construction of such parsers is transparent and easy. Their main
  application is the parsing of structured text files like those generated by
  laboratory instruments. Based on a paper by Hutton (1992)
  <doi:10.1017/S0956796800000411>. 
	"""
	
	homepage = "https://github.com/SystemsBioinformatics/parcr"
	cran = "parcr" 

	version("0.5.1", md5="efab25df663f17c4bca04b3a761b63b7")

	depends_on("r@4.1:", type=("build", "run"))
