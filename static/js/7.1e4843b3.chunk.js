(window.webpackJsonp=window.webpackJsonp||[]).push([[7],{286:function(e,t,a){"use strict";a.r(t);var n=a(6),l=a(7),s=a(9),i=a(8),c=a(10),r=a(11),o=a(1),u=a.n(o),g=a(3),d=a(46),m=a.n(d),h=(a(212),a(213),function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(s.a)(this,Object(i.a)(t).call(this,e))).state={userID:sessionStorage.getItem("user_id"),reviews:[{rid:1,reid:3,rname:"Metro Pizza",uid:6,content:"pizza is poor and the only food I'm satisfied with is the bottled water",star:2.5,create_time:"2018/10/9 19:04:11"},{rid:2,reid:1,rname:"Metro Pizza",uid:6,content:"Fair pizza, poor service",star:3,create_time:"2018/11/2 12:04:11"}],modal:!1,success:!1,warning:!1},a.deleteReview=a.deleteReview.bind(Object(r.a)(Object(r.a)(a))),a.toggle=a.toggle.bind(Object(r.a)(Object(r.a)(a))),a.toggleSuccess=a.toggleSuccess.bind(Object(r.a)(Object(r.a)(a))),a.toggleWarning=a.toggleWarning.bind(Object(r.a)(Object(r.a)(a))),a.updateReviews=a.updateReviews.bind(Object(r.a)(Object(r.a)(a))),a.updateReviews(),a}return Object(c.a)(t,e),Object(l.a)(t,[{key:"toggle",value:function(){this.setState({modal:!this.state.modal})}},{key:"toggleSuccess",value:function(){this.setState({success:!this.state.success})}},{key:"toggleWarning",value:function(){this.setState({warning:!this.state.warning})}},{key:"updateReviews",value:function(){var e=this;m.a.get("http://localhost:8080/api/review/"+this.state.userID).then(function(t){e.setState({reviews:t.data})},function(e){console.log(e)})}},{key:"deleteReview",value:function(e){var t=this;void 0==this.state.userID?window.alert("You have not login yet, please login first!"):m.a.delete("http://localhost:8080/api/review/"+this.state.userID,{data:{reid:e}}).then(function(e){t.toggleSuccess(),t.updateReviews()},function(e){console.log(e)})}},{key:"render",value:function(){var e=this;return u.a.createElement("div",{className:"animated fadeIn normal-wrapper"},u.a.createElement("h1",null,"Reviews"),u.a.createElement(g.J,null,this.state.reviews.map(function(t,a){return u.a.createElement(g.l,{lg:"6",key:a},u.a.createElement(g.e,null,u.a.createElement(g.f,null,u.a.createElement("h5",null,t.rname),u.a.createElement("h4",null,u.a.createElement("b",null,'"',t.content,'"')),u.a.createElement("h6",null,u.a.createElement("strong",null,"Star: "),t.star),u.a.createElement("h6",null,u.a.createElement("strong",null,"Create_time: "),t.create_time),u.a.createElement(g.d,{className:"d-inline-flex btn-small btn-pill float-right btn-outline-danger",onClick:e.deleteReview.bind(e,t.reid)},"Delete"))))}),u.a.createElement(g.C,{isOpen:this.state.success,toggle:this.toggleSuccess,className:"modal-success "+this.props.className},u.a.createElement(g.F,{toggle:this.toggleSuccess},"Delete Success"),u.a.createElement(g.D,null,"Your review has been removed."),u.a.createElement(g.E,null,u.a.createElement(g.d,{color:"success",onClick:this.toggleSuccess},"OK")," ")),u.a.createElement(g.C,{isOpen:this.state.warning,toggle:this.toggleWarning,className:"modal-warning "+this.props.className},u.a.createElement(g.F,{toggle:this.toggleWarning},"Review Fail"),u.a.createElement(g.D,null,"Please provide un-empty reviews."),u.a.createElement(g.E,null,u.a.createElement(g.d,{color:"warning",onClick:this.toggleWarning},"OK")," ",u.a.createElement(g.d,{color:"secondary",onClick:this.toggleWarning},"Cancel")))))}}]),t}(o.Component));t.default=h}}]);
//# sourceMappingURL=7.1e4843b3.chunk.js.map