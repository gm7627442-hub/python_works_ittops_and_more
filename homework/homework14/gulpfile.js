const gulp = require('gulp');
const imagemin = require('gulp-imagemin');

function compressImages() {
    return gulp.src('src/images/*')
        .pipe(imagemin())
        .pipe(gulp.dest('dist/images/'));
}

exports.default = compressImages;