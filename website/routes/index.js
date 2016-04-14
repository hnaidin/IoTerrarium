var express = require('express');
var passport = require('passport');
var Account = require('../models/account');
var router = express.Router();


router.get('/', function (req, res) {
    res.render('index', { user : req.user });
});

router.get('/register', function(req, res) {
    res.render('register', { user: req.user });
});

router.post('/register', function(req, res, next) {
    Account.register(new Account({ username : req.body.username }), req.body.password, function(err, account) {
        if (err) {
          return res.render("register", {info: "Sorry. That username already exists. Try again."});
        }

        passport.authenticate('local')(req, res, function () {
            req.session.save(function (err) {
                if (err) {
                    return next(err);
                }
                res.redirect('/');
            });
        });
    });
});


router.get('/login', function(req, res) {
    res.render('login', { user : req.user, message : req.flash('error')});
});

router.post('/login', passport.authenticate('local', { failureRedirect: '/login', failureFlash: true }), function(req, res, next) {
    req.session.save(function (err) {
        if (err) {
            return next(err);
        }
        res.redirect('/');
    });
});

router.get('/logout', function(req, res, next) {
    req.logout();
    req.session.save(function (err) {
        if (err) {
            return next(err);
        }
        res.redirect('/');
    });
});


router.get('/temp', function (req, res) {
    var sys = require('sys')
    var exec = require('child_process').exec;
    var child;
    // executes `pwd`
    script_location = "/home/pi/IoTerrarium/scripts/get_temp.py"
    script_interpreter = "python "
    child = exec(script_interpreter + script_location, function (error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
            console.log('exec error: ' + error);
        }
        res.render('temp', { user: req.user, data: stdout, error: error});
    });
});

router.get('/feed', function (req, res) {
    var sys = require('sys')
    var exec = require('child_process').exec;
    var child;
    // executes `pwd`
    script_location = "/home/pi/IoTerrarium/scripts/do_feed.py"
    child = exec("pwd", function (error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
            console.log('exec error: ' + error);
        }
        res.render('feed', { user: req.user, data: stdout, error: error });
    });
});

module.exports = router;
