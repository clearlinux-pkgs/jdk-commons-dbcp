Name     : jdk-commons-dbcp
Version  : 1.4
Release  : 4
URL      : https://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.jar
Source0  : https://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.jar
Source1  : https://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-commons-dbcp-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-commons-dbcp package.
Group: Data

%description data
data components for the jdk-commons-dbcp package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/commons-dbcp.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/commons-dbcp.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/commons-dbcp.xml \
%{buildroot}/usr/share/maven-poms/commons-dbcp.pom \
%{buildroot}/usr/share/java/commons-dbcp.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/commons-dbcp.jar
/usr/share/maven-metadata/commons-dbcp.xml
/usr/share/maven-poms/commons-dbcp.pom
