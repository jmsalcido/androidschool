import angular from 'angular';
import 'angular-mocks';
import title from './title.js';

describe('title component', function () {
  beforeEach(function () {
    angular
      .module('fountainTitle', ['src/app/title.html'])
      .component('fountainTitle', title);
    angular.mock.module('fountainTitle');
  });

  it('should render \'Allo, \'Allo!', angular.mock.inject(function ($rootScope, $compile) {
    var element = $compile('<fountain-title></fountain-title>')($rootScope);
    $rootScope.$digest();
    var title = element.find('h1');
    expect(title.html().trim()).toEqual('\'Allo, \'Allo!');
  }));
});
