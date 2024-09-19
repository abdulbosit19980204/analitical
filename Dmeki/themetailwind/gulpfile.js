var gulp = require('gulp');
var postcss = require('gulp-postcss');
var tailwindcss = require('tailwindcss');
var sass = require('gulp-sass')(require('sass'));
var autoprefixer = require('autoprefixer');
var pug = require('gulp-pug');
var browserSync = require('browser-sync').create();

// scss to css
gulp.task('style', function(){
  var processors = [
      tailwindcss,
      autoprefixer
  ];
  return gulp.src('assets/scss/**/*.scss',{sourcemaps:false})
    .pipe(sass({
      // outputStyle: 'compressed'
    }).on('error', sass.logError))
    .pipe(postcss(processors)) 
    .pipe(gulp.dest('assets/css', { sourcemaps: '.' }))
    .pipe(browserSync.reload({stream: true}));      
});

// pug to html 
gulp.task('html',function() {
   return gulp.src('assets/pug/pages/**.pug')
    .pipe(pug({ pretty: true }))
    .on('error', console.error.bind(console))
    .pipe(gulp.dest('html'))
    .pipe(browserSync.reload({stream: true}))
});

// watch task
gulp.task('watch', function(){
  browserSync.init({
      proxy: "http://localhost/tailwind-theme/dmeki/html/index.html"
  });   
  gulp.watch('assets/pug/pages/**.pug', gulp.series(['html']));  
  gulp.watch('assets/scss/**/*.scss', gulp.series(['style']));
})