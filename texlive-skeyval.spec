%global tl_name skeyval
%global tl_revision 30560

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Key-value parsing combining features of xkeyval and pgfkeys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skeyval
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skeyval.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skeyval.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package integrates the features of xkeyval and of pgfkeys by
introducing a new type of handlers. Style keys, links, changing key
callbacks and values on the fly, and other features of pgfkeys are
introduced in a new context.

