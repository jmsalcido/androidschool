import angular from 'angular';
import 'angular-mocks';
import footer from './footer.js';

describe('footer component', function () {
  beforeEach(function () {
    angular
      .module('fountainFooter', ['src/app/footer.html'])
      .component('fountainFooter', footer);
    angular.mock.module('fountainFooter');
  });

  it('should render \'FountainJS team\'', angular.mock.inject(function ($rootScope, $compile) {
    var element = $compile('<fountain-footer></fountain-footer>')($rootScope);
    $rootScope.$digest();
    var footer = element.find('a');
    expect(footer.html().trim()).toEqual('FountainJS team');
  }));
});
