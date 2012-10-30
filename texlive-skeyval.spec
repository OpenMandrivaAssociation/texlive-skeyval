# revision 28005
# category Package
# catalog-ctan /macros/latex/contrib/skeyval
# catalog-date 2012-10-15 16:33:02 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-skeyval
Version:	1.1
Release:	1
Summary:	Extensions to xkeyval
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skeyval
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeyval.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeyval.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package integrates the features of xkeyval and of pgfkeys
by introducing a new type of handlers. Style keys, links,
changing key callbacks and values on the fly, and other
features of pgfkeys are introduced in a new context.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skeyval/skeyval-bc.sty
%{_texmfdistdir}/tex/latex/skeyval/skeyval-core.tex
%{_texmfdistdir}/tex/latex/skeyval/skeyval-for.tex
%{_texmfdistdir}/tex/latex/skeyval/skeyval-ltxcmds.tex
%{_texmfdistdir}/tex/latex/skeyval/skeyval-ltxpatch.sty
%{_texmfdistdir}/tex/latex/skeyval/skeyval-pstkey.sty
%{_texmfdistdir}/tex/latex/skeyval/skeyval-pstkey.tex
%{_texmfdistdir}/tex/latex/skeyval/skeyval-view.sty
%{_texmfdistdir}/tex/latex/skeyval/skeyval.sty
%doc %{_texmfdistdir}/doc/latex/skeyval/README
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-pokayoke1.pdf
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-pokayoke1.tex
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-pokayoke2.pdf
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-pokayoke2.tex
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-testclass.cls
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-testpkg.sty
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-view-pokayoke1.pdf
%doc %{_texmfdistdir}/doc/latex/skeyval/skeyval-view-pokayoke1.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
