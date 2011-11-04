# revision 18494
# category Package
# catalog-ctan /macros/latex/contrib/skeyval
# catalog-date 2010-05-25 22:04:49 +0200
# catalog-license lppl1.3
# catalog-version 0.72
Name:		texlive-skeyval
Version:	0.72
Release:	1
Summary:	Extensions to xkeyval
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skeyval
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeyval.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeyval.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides several extensions to the xkeyval,
including new key types, and key management methods.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skeyval/skeyval.sty
%doc %{_texmfdistdir}/doc/latex/skeyval/README
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-guide.pdf
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-guide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
