const gulp = require("gulp");
const browserify = require("browserify");
const buffer = require("vinyl-buffer");
const cssmin = require('gulp-cssmin');
const fancy_log = require("fancy-log");
const sass = require('gulp-sass')(require('sass'));
const source = require("vinyl-source-stream");
const sourcemaps = require("gulp-sourcemaps");
const terser = require("gulp-terser");
const tsify = require("tsify");
const watchify = require("watchify");

require('dotenv').config();

const debug = (String(process.env.DEBUG).toLowerCase() === "true");
const paths = {
  dest: "{{ project_name }}_app/static/{{ project_name }}_app/dist",
  scripts: {
    entries: ["src/main.ts"],
    outfile: "{{ project_name }}.bundle.min.js"
  },
  styles: {
    src: "src/**/*.*css"
  }
};

var browserifyObj = browserify({
  basedir: ".",
  debug: debug,
  entries: paths.scripts.entries,
  cache: {},
  packageCache: {},
}).plugin(tsify)

function scripts() {
  return browserifyObj
    .bundle()
    .on("error", fancy_log)
    .pipe(source(paths.scripts.outfile))
    .pipe(buffer())
    .pipe(sourcemaps.init({ loadMaps: true }))
    .pipe(terser({
      mangle: true
    }))
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest(paths.dest));
}

function styles() {
  return gulp.src(paths.styles.src, { sourcemaps: true })
    .pipe(sass())
    .pipe(cssmin())
    .pipe(gulp.dest(paths.dest));
}

function watch() {
  var watchedBrowserify = watchify(browserifyObj);
  scripts();
  watchedBrowserify.on("update", scripts);
  watchedBrowserify.on("log", fancy_log);
  gulp.watch(paths.styles.src, styles);
}

exports.build = gulp.parallel(scripts, styles);
exports.default = exports.build;
exports.watch = watch;
