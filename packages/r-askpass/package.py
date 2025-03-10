# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAskpass(RPackage):
	"""Safe Password Entry for R, Git, and SSH.

	Cross-platform utilities for prompting the user for credentials or a
	passphrase, for example to authenticate with a server or read a protected
	key. Includes native programs for MacOS and Windows, hence no 'tcltk' is
	required. Password entry can be invoked in two different ways: directly
	from R via the askpass() function, or indirectly as password-entry back-end
	for 'ssh-agent' or 'git-credential' via the SSH_ASKPASS and GIT_ASKPASS
	environment variables. Thereby the user can be prompted for credentials or
	a passphrase if needed when R calls out to git or ssh."""

	cran = "askpass"

	version("1.2.0", md5="59d2bbfe6bd3a7bf05d56006f1cb1d6a")

	depends_on("r-sys@2.1:", type=("build", "run"))
