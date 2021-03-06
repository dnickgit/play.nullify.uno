import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('home');
  this.route('challenges');
  this.route('scoreboard');
  this.route('about');
  this.route('modal');
  this.route('404', {path: "*path"});
});

export default Router;
