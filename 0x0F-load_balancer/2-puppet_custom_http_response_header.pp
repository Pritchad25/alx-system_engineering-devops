# This script installs and configures a Nginx server using Puppet
package { 'nginx':
	ensure => 'installed',
}

file { '/var/www/html/index.html':
	ensure  => 'file',
	content => 'Hello World!',
	require => Package['nginx'],
}

# The code below ensures that the Nginx service is running and enabled
service { 'nginx':
	ensure  => 'running',
	enable  => true,
	require => Package['nginx'],
}

file_line { 'add_header':
	ensure  => 'present',
	path    => '/etc/nginx/sites-available/default',
	line    => "add_header X-Served-By ${hostname};",
	after   => 'server_name _;',
	require => Service['nginx'],
}

exec { 'restart nginx':
	command     => '/usr/sbin/service nginx restart',
}
