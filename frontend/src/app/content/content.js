export default {
  templateUrl: 'src/app/content/content.html',
  controller: [ContentController],
  bindings: {
    content: '<'
  }
};

function ContentController() {
  var vm = this;

  vm.menus = [{
    title: "Slides",
    url: "#/slides"
  }, {
    title: "Mentors",
    url: "#/mentors"
  }, {
    title: "Blog",
    url: "#/blog"
  }, {
    title: "GitHub",
    url: "http://github.com/nearsoft"
  }];

  vm.slides = [{
    title: "Day 1: Android",
    url: "http://slides.com/josesalcido-1/android/fullscreen"
  }, {
    title: "Day 2: Java & The Object Oriented Programming Principle",
    url: "http://slides.com/josesalcido-1/object-oriented-programming/fullscreen"
  }, {
    title: "Day 3: Activities & Fragments",
    url: "#not-ready"
  }, {
    title: "Day 3: Views & Beyond",
    url: "http://slides.com/josesalcido-1/deck-3/fullscreen"
  }];

}
