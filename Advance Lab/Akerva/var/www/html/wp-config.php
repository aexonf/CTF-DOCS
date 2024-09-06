<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wordpress' );

/** MySQL database password */
define( 'DB_PASSWORD', 'ZokDHE_DJ_____enzU)=' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'HcgYQU?EfUu2<eBLHt`Or/!>KbcZ_%z>q!H6R:Fk(aq-moIg]E%@rjfE>;?~D0}k' );
define( 'SECURE_AUTH_KEY',  'v9>ZRo-By<QIk8?JK3|TgCRBa17|}.mDfFc;{6lBlvXZ}&>Ke_oz(*[`rL{K`+`J' );
define( 'LOGGED_IN_KEY',    'L8x)P: Il)F0q|q{|A<4h)gkb7yxUFXi`s%gAwMwvBP(Gu] 3pqztI(Shh$I) !J' );
define( 'NONCE_KEY',        'C3Rul|DDxi%mzLmZZxg$ku}:fo:S<(|| 1A)f-T(&.1PW>.a@>NmuMpv4x{PHI~c' );
define( 'AUTH_SALT',        'v);3noXf.`D&_vNH?%cd=Y54@0}B$e^/)ZRN^3uP}lyUWgN-~iR,W&Vlh(2n.1aj' );
define( 'SECURE_AUTH_SALT', '4$Wk=b@;^f}5^^Laxlpn33{Bk[Vo|dh(!J),2( Ypc40`=`G+%<UFeJR~z4-D{+@' );
define( 'LOGGED_IN_SALT',   '9feEWeQN[rwZ|CMd~Y/E4v9;?H4F)retX3cfn=F$F5Rh2`S#c*TBIayY=^EX#6)v' );
define( 'NONCE_SALT',       'TX1x>7?pkn4H96c~JHn)9StD~b+LG}X.,v%:@+$Fg2DpH1mYB=RVY~tUd: -{}R6' );
define( 'DISALLOW_FILE_MODS', true);

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
