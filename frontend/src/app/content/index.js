import angular from 'angular';

import content from './content.js';

var contentModule = 'content';

export default contentModule;

angular
  .module(contentModule, [])
  .component('schoolContent', content);
