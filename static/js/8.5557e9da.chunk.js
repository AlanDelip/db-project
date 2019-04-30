(window.webpackJsonp=window.webpackJsonp||[]).push([[8],{214:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.focusableElements=t.defaultToggleEvents=t.canUseDOM=t.PopperPlacements=t.keyCodes=t.TransitionStatuses=t.TransitionPropTypeKeys=t.TransitionTimeouts=t.targetPropType=void 0;var a="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e};t.getScrollbarWidth=s,t.setScrollbarWidth=l,t.isBodyOverflowing=c,t.getOriginalBodyPadding=function(){var e=window.getComputedStyle(document.body,null);return parseInt(e&&e.getPropertyValue("padding-right")||0,10)},t.conditionallyUpdateScrollbar=function(){var e=s(),t=document.querySelectorAll(".fixed-top, .fixed-bottom, .is-fixed, .sticky-top")[0],n=t?parseInt(t.style.paddingRight||0,10):0;c()&&l(n+e)},t.setGlobalCssModule=function(e){u=e},t.mapToCssModules=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:u;return t?e.split(" ").map(function(e){return t[e]||e}).join(" "):e},t.omit=function(e,t){var n={};return Object.keys(e).forEach(function(a){-1===t.indexOf(a)&&(n[a]=e[a])}),n},t.pick=function(e,t){var n=Array.isArray(t)?t:[t],a=n.length,o=void 0,r={};for(;a>0;)o=n[a-=1],r[o]=e[o];return r},t.warnOnce=g,t.deprecated=function(e,t){return function(n,a,o){null!==n[a]&&"undefined"!==typeof n[a]&&g('"'+a+'" property of "'+o+'" has been deprecated.\n'+t);for(var r=arguments.length,i=Array(r>3?r-3:0),s=3;s<r;s++)i[s-3]=arguments[s];return e.apply(void 0,[n,a,o].concat(i))}},t.DOMElement=f,t.isReactRefObj=h,t.findDOMElements=p,t.isArrayOrNodeList=b,t.getTarget=function(e){var t=p(e);if(b(t))return t[0];return t},t.addMultipleEventListeners=function(e,t,n){var a=e;b(a)||(a=[a]);var o=n;"string"===typeof o&&(o=o.split(/\s+/));if(!b(a)||"function"!==typeof t||!Array.isArray(o))throw new Error("\n      The first argument of this function must be DOM node or an array on DOM nodes or NodeList.\n      The second must be a function.\n      The third is a string or an array of strings that represents DOM events\n    ");return o.forEach(function(e){a.forEach(function(n){n.addEventListener(e,t)})}),function(){o.forEach(function(e){a.forEach(function(n){n.removeEventListener(e,t)})})}};var o=i(n(80)),r=i(n(0));function i(e){return e&&e.__esModule?e:{default:e}}function s(){var e=document.createElement("div");e.style.position="absolute",e.style.top="-9999px",e.style.width="50px",e.style.height="50px",e.style.overflow="scroll",document.body.appendChild(e);var t=e.offsetWidth-e.clientWidth;return document.body.removeChild(e),t}function l(e){document.body.style.paddingRight=e>0?e+"px":null}function c(){return document.body.clientWidth<window.innerWidth}var u=void 0;var d={};function g(e){d[e]||("undefined"!==typeof console&&console.error(e),d[e]=!0)}function f(e,t,n){if(!(e[t]instanceof Element))return new Error("Invalid prop `"+t+"` supplied to `"+n+"`. Expected prop to be an instance of Element. Validation failed.")}t.targetPropType=r.default.oneOfType([r.default.string,r.default.func,f,r.default.shape({current:r.default.any})]),t.TransitionTimeouts={Fade:150,Collapse:350,Modal:300,Carousel:600},t.TransitionPropTypeKeys=["in","mountOnEnter","unmountOnExit","appear","enter","exit","timeout","onEnter","onEntering","onEntered","onExit","onExiting","onExited"],t.TransitionStatuses={ENTERING:"entering",ENTERED:"entered",EXITING:"exiting",EXITED:"exited"},t.keyCodes={esc:27,space:32,enter:13,tab:9,up:38,down:40},t.PopperPlacements=["auto-start","auto","auto-end","top-start","top","top-end","right-start","right","right-end","bottom-end","bottom","bottom-start","left-end","left","left-start"];var m=t.canUseDOM=!("undefined"===typeof window||!window.document||!window.document.createElement);function h(e){return!(!e||"object"!==("undefined"===typeof e?"undefined":a(e)))&&"current"in e}function p(e){if(h(e))return e.current;if((0,o.default)(e))return e();if("string"===typeof e&&m){var t=document.querySelectorAll(e);if(t.length||(t=document.querySelectorAll("#"+e)),!t.length)throw new Error("The target '"+e+"' could not be identified in the dom, tip: check spelling");return t}return e}function b(e){return null!==e&&(Array.isArray(e)||m&&"number"===typeof e.length)}t.defaultToggleEvents=["touchstart","click"];t.focusableElements=["a[href]","area[href]","input:not([disabled]):not([type=hidden])","select:not([disabled])","textarea:not([disabled])","button:not([disabled])","object","embed","[tabindex]:not(.modal)","audio[controls]","video[controls]",'[contenteditable]:not([contenteditable="false"])']},292:function(e,t,n){"use strict";n.r(t);var a=n(6),o=n(7),r=n(9),i=n(8),s=n(10),l=n(11),c=n(1),u=n.n(c),d=n(3),g=n(47),f=n(2),m=n.n(f),h=n(214),p=function(e){function t(){return Object(a.a)(this,t),Object(r.a)(this,Object(i.a)(t).apply(this,arguments))}return Object(s.a)(t,e),Object(o.a)(t,[{key:"render",value:function(){var e=this.props,t=e.className,n=e.cssModule,a=e.header,o=e.icon,r=e.color,i=e.value,s=e.children,l=e.invert,c=Object(g.a)(e,["className","cssModule","header","icon","color","value","children","invert"]),f={style:"",color:r,value:i},p={style:"",bgColor:"",icon:o};l&&(f.style="progress-white",f.color="",p.style="text-white",p.bgColor="bg-"+r);var b=Object(h.mapToCssModules)(m()(t,p.style,p.bgColor),n);return f.style=m()("progress-xs mt-3 mb-0",f.style),u.a.createElement(d.e,Object.assign({className:b},c),u.a.createElement(d.f,null,u.a.createElement("div",{className:"h1 text-muted text-right mb-2"},u.a.createElement("i",{className:p.icon})),u.a.createElement("div",{className:"h4 mb-0"},a),u.a.createElement("small",{className:"text-muted text-uppercase font-weight-bold"},s)))}}]),t}(c.Component);p.defaultProps={header:"87.500",icon:"icon-people",color:"info",value:"25",children:"Visitors",invert:!1};var b=p,y=(n(212),n(213),n(46)),E=n.n(y),v=function(e){function t(e){var n;return Object(a.a)(this,t),(n=Object(r.a)(this,Object(i.a)(t).call(this,e))).state={userID:sessionStorage.getItem("user_id"),friends:[{uid:1,uname:"Mengyu Han",connected_time:"2018/10/9 19:04:11"},{uid:2,uname:"Zhufeng Xu",connected_time:"2018/10/9 19:04:11"}],modal:!1,success:!1,warning:!1,info:!1,searchSuccess:!1},n.updateFriends=n.updateFriends.bind(Object(l.a)(Object(l.a)(n))),n.deleteFriend=n.deleteFriend.bind(Object(l.a)(Object(l.a)(n))),n.addFriend=n.addFriend.bind(Object(l.a)(Object(l.a)(n))),n.toggle=n.toggle.bind(Object(l.a)(Object(l.a)(n))),n.toggleSuccess=n.toggleSuccess.bind(Object(l.a)(Object(l.a)(n))),n.toggleSearchSuccess=n.toggleSearchSuccess.bind(Object(l.a)(Object(l.a)(n))),n.toggleWarning=n.toggleWarning.bind(Object(l.a)(Object(l.a)(n))),n.toggleInfo=n.toggleInfo.bind(Object(l.a)(Object(l.a)(n))),n.updateFriends(),n}return Object(s.a)(t,e),Object(o.a)(t,[{key:"updateFriends",value:function(){var e=this;E.a.get("http://localhost:8080/api/friend/"+this.state.userID).then(function(t){e.setState({friends:t.data})},function(e){console.log(e)})}},{key:"toggle",value:function(){this.setState({modal:!this.state.modal})}},{key:"toggleSuccess",value:function(){this.setState({success:!this.state.success})}},{key:"toggleWarning",value:function(){this.setState({warning:!this.state.warning})}},{key:"toggleInfo",value:function(){void 0==this.state.userID?window.alert("You have not login yet, please login first!"):this.setState({info:!this.state.info})}},{key:"toggleSearchSuccess",value:function(){this.setState({searchSuccess:!this.state.searchSuccess})}},{key:"deleteFriend",value:function(e){var t=this;void 0==this.state.userID?window.alert("You have not login yet, please login first!"):E.a.delete("http://localhost:8080/api/friend/"+this.state.userID,{data:{uid_friend:e}}).then(function(e){t.toggleSuccess(),t.updateFriends()},function(e){t.toggleWarning()})}},{key:"addFriend",value:function(){var e=this,t=document.getElementById("searchUserName").value;E.a.post("http://localhost:8080/api/friend/"+this.state.userID,{uname_friend:t}).then(function(t){t.data?(e.toggleInfo(),e.toggleSearchSuccess(),e.updateFriends()):window.alert("Not valid user")},function(t){e.toggleWarning()})}},{key:"render",value:function(){var e=this;return u.a.createElement("div",{className:"animated fadeIn normal-wrapper"},u.a.createElement("h1",null,"Friends"),u.a.createElement(d.J,null,this.state.friends.map(function(t,n){return u.a.createElement(d.l,{key:n,xs:"12",sm:"6",lg:"3"},u.a.createElement("div",null,u.a.createElement(b,{icon:"icon-people",color:"info",header:t.uname},"Connect time:"+t.connected_time,u.a.createElement("br",null),u.a.createElement("br",null),u.a.createElement(d.d,{className:"d-block btn-small btn-round float-right btn-outline-danger",onClick:e.deleteFriend.bind(e,t.uid)},"Delete"))))}),u.a.createElement(d.l,{xs:"12",sm:"6",lg:"3"},u.a.createElement(b,{onClick:this.toggleInfo,icon:"icon-user-follow text-white",className:"bg-primary",color:"info",style:{cursor:"pointer"},header:"Add a Friend"},u.a.createElement("br",null),u.a.createElement("br",null),u.a.createElement("br",null))),u.a.createElement(d.C,{isOpen:this.state.success,toggle:this.toggleSuccess,className:"modal-success "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleSuccess},"Delete Success"),u.a.createElement(d.D,null,"You will not see the user in your user list any more."),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"success",onClick:this.toggleSuccess},"OK")," ")),u.a.createElement(d.C,{isOpen:this.state.info,toggle:this.toggleInfo,className:"modal-info "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleInfo},"Search User"),u.a.createElement(d.D,null,u.a.createElement(d.t,null,u.a.createElement(d.z,{htmlFor:"ccmonth"},"Please enter user name"),u.a.createElement(d.v,null,u.a.createElement(d.w,{addonType:"prepend"},u.a.createElement(d.d,{type:"button",color:"primary",onClick:this.addFriend},u.a.createElement("i",{className:"fa fa-search"})," Search")),u.a.createElement(d.u,{type:"text",id:"searchUserName",placeholder:"Username"})))),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"secondary",onClick:this.toggleInfo},"Cancel"))),u.a.createElement(d.C,{isOpen:this.state.warning,toggle:this.toggleWarning,className:"modal-warning "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleWarning},"Duplicate Operation"),u.a.createElement(d.D,null,"This user has already been your friend."),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"warning",onClick:this.toggleWarning},"OK")," ",u.a.createElement(d.d,{color:"secondary",onClick:this.toggleWarning},"Cancel"))),u.a.createElement(d.C,{isOpen:this.state.searchSuccess,toggle:this.toggleSearchSuccess,className:"modal-success "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleSearchSuccess},"Delete Success"),u.a.createElement(d.D,null,"You have successfully add the user to your friend list."),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"success",onClick:this.toggleSearchSuccess},"OK")," "))))}}]),t}(c.Component);t.default=v}}]);
//# sourceMappingURL=8.5557e9da.chunk.js.map