import Ember from 'ember';

export default Ember.Component.extend({
  modal: {},
  authController: null,
  email: '',
  teamname: '',
  password: '',
  confirmPassword: '',
  classNames: ['login-box-margin'],
  setupKeys: function() {
    Ember.$('body').on('keyup.modal-dialog', (e) => {
      if (e.keyCode === 27) {
        this.set('modal.isRegister', false);
      }
    });
  }.on('didInsertElement'),
  teardownKeys: function() {
    Ember.$('body').off('keyup.modal-dialog');
  }.on('willDestroyElement'),
  setupFocus: function() {
    Ember.$('#inputEmail').focus();
  }.on('didInsertElement'),
  actions: {
    submitRegister: function() {
      var email = this.get('email');
      var username = this.get('username');
      var teamname = this.get('teamname');
      var password = this.get('password');
      var confirmpassword = this.get('confirmPassword');
      this.sendAction('sendRegister', {'email': email, 'username': username, 'teamname': teamname, 'password': password, 'confirmPassword': confirmpassword });
    },
    openRegisterModal: function() {
      this.set('modal.isRegister', true);
    },
    closeRegisterModal: function() {
      this.set('modal.isRegister', false);
      this.get('authController').set('errorMessage', '');
      this.get('authController').set('errorFields', {});
    },
    registerToLoginModal: function(){
      this.set('modal.isRegister', false);
      this.set('modal.isLogin', true);
      this.get('authController').set('errorMessage', '');
      this.get('authController').set('errorFields', {});
    },
  }
});