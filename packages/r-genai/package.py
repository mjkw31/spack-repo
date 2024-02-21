# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenai(RPackage):
	"""Generative Artificial Intelligence

	Utilizing 'Generative Artificial Intelligence' models like 'GPT-4' and 'Gemini Pro' as coding and writing assistants for 'R' users. Through these models, 'GenAI' offers a variety of functions, encompassing text generation, code optimization, natural language processing, chat, and image interpretation. The goal is to aid 'R' users in streamlining laborious coding and language processing tasks.
	"""
	
	homepage = "https://genai.gd.edu.kg/"
	cran = "GenAI" 

	version("0.1.15", md5="75fca9b58d169b3986ef8a0e7919ef3c")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
