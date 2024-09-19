var gulp = require('gulp');
var sass = require('gulp-sass')(require('sass'));
// var autoprefixer = require('gulp-autoprefixer');
var pug = require('gulp-pug');
var browserSync = require('browser-sync').create();

// scss to css
gulp.task('style', function(){
  return gulp.src('assets/scss/**/*.scss',{sourcemaps:false})
   	.pipe(sass({
       // outputStyle: 'compressed' //If Convert normal style so remove this line
    }).on('error', sass.logError))
    // .pipe(autoprefixer('last 2 versions'))
    .pipe(gulp.dest('assets/css', { sourcemaps: '.' }))
    .pipe(browserSync.reload({stream: true})); 			
});

// pug to html 
gulp.task('html',function(){
   return gulp.src('assets/pug/pages/**.pug')
	  .pipe(pug({ pretty: true }))
	  .on('error', console.error.bind(console))
	  .pipe(gulp.dest('html'))
	  .pipe(browserSync.reload({stream: true}))
});

// watch task
gulp.task('watch', function(){
	browserSync.init({
	    proxy: "http://localhost/my-theme/dmeki/html/index.html"
	});   
  gulp.watch('assets/scss/**/*.scss', gulp.series(['style']));
  gulp.watch('assets/pug/pages/**.pug', gulp.series(['html']));  
})




