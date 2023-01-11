class Inadyn < Formula
  desc "Dynamic DNS client with IPv4, IPv6, and SSL/TLS support"
  homepage "http://troglobit.com/projects/inadyn/"
  url "https://github.com/troglobit/inadyn/releases/download/v2.5/inadyn-2.5.tar.gz"
  sha256 "f7faf0be4f0b4bfa1acc811189a9ed0a58bc367e48ea31c283920a2ef27cdc40"
  version "2.5"

  head do
    url "https://github.com/troglobit/inadyn.git"
  end

  depends_on "autoconf" => :build
  depends_on "automake" => :build
  depends_on "cmake"    => :build
  depends_on "libtool"  => :build
  depends_on "confuse"
  depends_on "gnutls"
  depends_on "pkg-config"

  # Fix for Sierra with v2.5, remove in next version
  patch do
    url "https://github.com/troglobit/inadyn/commit/57bdcc0321b49ee68397c70140d9895655edb06f.diff?full_index=1"
    sha256 "6d24c3822e7017a471583f5424421d83e6e426b464ca7521db943ecec580eea5"
  end

  def install
    mkdir_p buildpath/"inadyn/m4"
    system "autoreconf", "-vif"
    system "./configure", "--disable-dependency-tracking",
                          "--disable-silent-rules",
                          "--prefix=#{prefix}",
                          "--sysconfdir=#{etc}",
                          "--localstatedir=#{var}"
    system "make", "install"
  end

  test do
    system "#{sbin}/inadyn", "--check-config", "--config=#{HOMEBREW_PREFIX}/share/doc/inadyn/examples/inadyn.conf"
  end
end
