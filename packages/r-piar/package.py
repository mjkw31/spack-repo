# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiar(RPackage):
	"""Price Index Aggregation

	Most price indexes are made with a two-step procedure, where
    period-over-period elemental indexes are first calculated for a collection
    of elemental aggregates at each point in time, and then aggregated according
    to a price index aggregation structure. These indexes can then be chained
    together to form a time series that gives the evolution of prices with
    respect to a fixed base period. This package contains a collections of
    functions that revolve around this work flow, making it easy to build
    standard price indexes, and implement the methods described by
    Balk (2008, ISBN:978-1-107-40496-0), von der Lippe (2001,
    ISBN:3-8246-0638-0), and the CPI manual (2020, ISBN:978-1-51354-298-0)
    for bilateral price indexes.
	"""
	
	homepage = "https://marberts.github.io/piar/"
	cran = "piar" 

	version("0.6.0", md5="0df88bb105a01aa00b6387942dbd4d55")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gpindex@0.5:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
