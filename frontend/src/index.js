import angular from 'angular';

import contentModule from './app/content/index.js';
import 'angular-ui-router';
import routesConfig from './routes.js';

import main from './app/main.js';
import header from './app/header.js';
import title from './app/title.js';
import footer from './app/footer.js';

angular
  .module('app', [contentModule, 'ui.router'])
  .config(routesConfig)
  .component('app', main)
  .component('schoolHeader', header)
  .component('schoolTitle', title)
  .component('schoolFooter', footer);
