import angular from 'angular';
import 'angular-mocks';
import header from './header.js';

describe('header component', function () {
  beforeEach(function () {
    angular
      .module('fountainHeader', ['src/app/header.html'])
      .component('fountainHeader', header);
    angular.mock.module('fountainHeader');
  });

  it('should render \'Fountain Generator\'', angular.mock.inject(function ($rootScope, $compile) {
    var element = $compile('<fountain-header></fountain-header>')($rootScope);
    $rootScope.$digest();
    var header = element.find('a');
    expect(header.html().trim()).toEqual('Fountain Generator');
  }));
});
