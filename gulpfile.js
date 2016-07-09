var gulp = require('gulp');
var path = require('path');
var plugins = require("gulp-load-plugins")({
	pattern: ['gulp-*', 'gulp.*', 'main-bower-files'],
	replaceString: /\bgulp[\-.]/
});
var sh = require('shelljs');
var dest = "web"
const spawn = require('child_process').spawn;

/**
* Limpiar librerias vendor
*/
gulp.task('clean', function(next) {
	sh.rm('-rf', path.join(dest, 'vendor', '*.*'));
	next();
});

gulp.task('copy', ['clean', 'copy-js-css', 'less', 'icons'], function(){});

/**
* Copiar desde bower_components
*/
gulp.task('copy-js-css', function() {
	const jsFilter = plugins.filter('**/*.js', {restore: true});
	const cssFilter = plugins.filter('**/*.css', {restore: true});
	gulp.src(plugins.mainBowerFiles())
	.pipe(jsFilter)
	.pipe(plugins.uglify())
	.pipe(gulp.dest(path.join(dest, 'vendor')));
	gulp.src(plugins.mainBowerFiles())
	.pipe(cssFilter)
	.pipe(plugins.uglify())
	.pipe(gulp.dest(path.join(dest, 'vendor')));
});

/**
* Compilar less
*/
gulp.task('less', function () {
	const lessFilter = plugins.filter('**/*.less', {restore: true});
 	gulp.src(plugins.mainBowerFiles())
	.pipe(lessFilter)
    .pipe(plugins.less())
	.pipe(gulp.dest(path.join(dest, 'vendor')));
});

/*
* Font Awesome Icons
*/
gulp.task('icons', function() {
    return gulp.src(path.join('bower_components', 'font-awesome','fonts', '**.*'))
    .pipe(gulp.dest(path.join(dest, 'fonts')));
});
