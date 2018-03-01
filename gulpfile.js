var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;


// sass
gulp.task('sass', function(){
    return gulp.src('app/scss/**/*.scss')  // get all file sending with .scss in app/scss
    .pipe(sass())  // converts Sass to CSS with gulp-sass
    .pipe(gulp.dest('themes/salasClean/static/css'))
});



// Static server
gulp.task('serve', ['pelican'], function() {
    browserSync.init({
        server: {
            baseDir: "output"
        }
    });
    // gulp.watch('content/**').on('change', browserSync.reload);
});






gulp.task('pelican', function(cb){
    exec('pelican', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    cb(err);
  });
});


gulp.task('watch', function(){
    //gulp.watch('app/scss/**/*.scss',['sass','pelican', browserSync.reload]);
    gulp.watch('content/**', ['pelican', browserSync.reload]);
});


// Move Fonts to
gulp.task('fonts', function() {
    return gulp.src('node_modules/font-awesome/fonts/*')
      //.pipe(gulp.dest('src/fonts'))
      .pipe(gulp.dest('themes/salasClean/static/fonts'))
  })
  
  // Move Font Awesome CSS to 
  gulp.task('fa', function() {
    return gulp.src('node_modules/font-awesome/css/font-awesome.min.css')
      //.pipe(gulp.dest('src/css'))
      .pipe(gulp.dest("themes/salasClean/static/css"))
  })


gulp.task('default', ['fa', 'fonts','pelican','watch','serve']);