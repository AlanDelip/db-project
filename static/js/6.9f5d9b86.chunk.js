(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{285:function(e,t,s){"use strict";s.r(t);var a=s(6),i=s(7),l=s(9),n=s(8),c=s(10),o=s(11),r=s(1),u=s.n(r),d=s(3),h=(s(212),s(213),s(46)),g=s.n(h),m=function(e){function t(e){var s;return Object(a.a)(this,t),(s=Object(l.a)(this,Object(n.a)(t).call(this,e))).state={userID:sessionStorage.getItem("user_id"),modal:!1,success:!1,warning:!1,info:!1,successAddWishList:!1,successDeleteRestaurant:!1,successDeleteWishList:!1,wishlist:[{wid:"1",name:"Default List",create_time:"2018/10/9 19:04:11",restaurants:[{rid:1,name:"Metro Pizza"},{rid:2,name:"Buddy V's Ristorante E Caffe"}]},{wid:"2",name:"My Favorite Pizza Restaurants",create_time:"2018/10/9 19:04:11",restaurants:[{rid:1,name:"Metro Pizza"},{rid:2,name:"Buddy V's Ristorante E Caffe"}]},{wid:"3",name:"Nearby Chinese Restaurants",create_time:"2018/10/9 19:04:11",restaurants:[{rid:1,name:"Metro Pizza"},{rid:2,name:"Buddy V's Ristorante E Caffe"}]}],collapse:!1,accordion:[!0,!1,!1],custom:[!0,!1],status:"Closed",fadeIn:!0,timeout:300},s.toggleInfo=s.toggleInfo.bind(Object(o.a)(Object(o.a)(s))),s.toggleAccordion=s.toggleAccordion.bind(Object(o.a)(Object(o.a)(s))),s.addWishList=s.addWishList.bind(Object(o.a)(Object(o.a)(s))),s.toggle=s.toggle.bind(Object(o.a)(Object(o.a)(s))),s.toggleSuccess=s.toggleSuccess.bind(Object(o.a)(Object(o.a)(s))),s.toggleWarning=s.toggleWarning.bind(Object(o.a)(Object(o.a)(s))),s.toggleSuccessAddWishList=s.toggleSuccessAddWishList.bind(Object(o.a)(Object(o.a)(s))),s.toggleDeleteRestaurantSuccess=s.toggleDeleteRestaurantSuccess.bind(Object(o.a)(Object(o.a)(s))),s.toggleSuccessDeleteWishList=s.toggleSuccessDeleteWishList.bind(Object(o.a)(Object(o.a)(s))),s.deleteRestaurant=s.deleteRestaurant.bind(Object(o.a)(Object(o.a)(s))),s.deleteWishList=s.deleteWishList.bind(Object(o.a)(Object(o.a)(s))),s.updateWishList=s.updateWishList.bind(Object(o.a)(Object(o.a)(s))),s.setUpAccording=s.setUpAccording.bind(Object(o.a)(Object(o.a)(s))),s.updateWishList(),s}return Object(c.a)(t,e),Object(i.a)(t,[{key:"setUpAccording",value:function(e){var t=[];t.push(!0);for(var s=1;s<e;s++)t.push(!1);this.setState({accordion:t})}},{key:"updateWishList",value:function(){var e=this;g.a.get("http://localhost:8080/api/wishlist/"+this.state.userID).then(function(t){e.setState({wishlist:t.data}),e.setUpAccording(e.state.wishlist.length)},function(e){console.log(e)})}},{key:"deleteRestaurant",value:function(e,t){var s=this;void 0==this.state.userID?window.alert("You have not login yet, please login first!"):g.a.delete("http://localhost:8080/api/wishlist/"+this.state.userID,{data:{wid:t,rid:e}}).then(function(e){s.toggleDeleteRestaurantSuccess(),s.updateWishList()},function(e){console.log(e)})}},{key:"deleteWishList",value:function(e){var t=this;void 0==this.state.userID?window.alert("You have not login yet, please login first!"):g.a.delete("http://localhost:8080/api/wishlist",{data:{wid:e,uid:this.state.userID}}).then(function(e){t.toggleSuccessDeleteWishList(),t.updateWishList()},function(e){console.log(e)})}},{key:"toggle",value:function(){void 0==this.state.userID?window.alert("You have not login yet, please login first!"):this.setState({modal:!this.state.modal})}},{key:"toggleSuccess",value:function(){this.setState({success:!this.state.success})}},{key:"toggleWarning",value:function(){this.setState({warning:!this.state.warning})}},{key:"toggleInfo",value:function(){this.setState({info:!this.state.info})}},{key:"toggleSuccessAddWishList",value:function(){this.setState({successAddWishList:!this.state.successAddWishList})}},{key:"toggleSuccessDeleteWishList",value:function(){this.setState({successDeleteWishList:!this.state.successDeleteWishList})}},{key:"toggleDeleteRestaurantSuccess",value:function(){this.setState({successDeleteRestaurant:!this.state.successDeleteRestaurant})}},{key:"addWishList",value:function(){var e=this;this.toggle();var t=document.getElementById("newWishListTextArea").value;g.a.post("http://localhost:8080/api/wishlist",{uid:this.state.userID,name:t}).then(function(t){e.toggleSuccess(),e.updateWishList()},function(e){console.log(e)})}},{key:"toggleAccordion",value:function(e){var t=this.state.accordion.map(function(t,s){return e===s&&!t});this.setState({accordion:t})}},{key:"render",value:function(){var e=this;return u.a.createElement("div",{className:"animated fadeIn normal-wrapper"},u.a.createElement("div",{className:"wishlist-wrapper"},u.a.createElement("h1",null,"Wishlist"),u.a.createElement("span",{onClick:function(){return e.toggle()},className:"create-wishlist bg-orange text-white"},u.a.createElement("i",{className:"fa fa-plus fa-adjust-aligh"}),u.a.createElement("span",null," Create Wishlist"))),u.a.createElement("div",{id:"accordion"},u.a.createElement(d.J,null,this.state.wishlist.map(function(t,s){return u.a.createElement(d.l,{lg:"6",key:s},u.a.createElement(d.e,null,u.a.createElement(d.i,{className:"bg-primary",id:"heading"+s},u.a.createElement(d.d,{block:!0,color:"link",className:"text-left m-0 p-0",onClick:function(){return e.toggleAccordion(s)},"aria-expanded":e.state.accordion[0],"aria-controls":"collapseOne"},u.a.createElement("h4",{className:"d-inline-block m-0 p-0 text-white"},"Wishlist ",s+1,": ",t.name)),u.a.createElement(d.d,{className:"btn-small btn-pill float-right btn-outline-light",onClick:e.deleteWishList.bind(e,t.wid)},"Delete")),u.a.createElement(d.m,{isOpen:e.state.accordion[s],"data-parent":"#accordion",id:"collapse"+s,"aria-labelledby":"heading"+s},u.a.createElement(d.f,null,u.a.createElement(d.A,null,t.restaurants.map(function(s,a){return u.a.createElement(d.B,{key:a,className:"border-left-0 border-right-0"},u.a.createElement("h5",{className:"d-inline-block"},s.name),u.a.createElement(d.d,{className:"d-inline-block btn-small btn-pill float-right btn-outline-danger",onClick:e.deleteRestaurant.bind(e,s.rid,t.wid)},"Delete"))}))))))}))),u.a.createElement(d.C,{isOpen:this.state.modal,toggle:this.toggle,className:this.props.className},u.a.createElement(d.F,{toggle:this.toggle},"New Wishlist"),u.a.createElement(d.D,null,u.a.createElement(d.t,{row:!0},u.a.createElement(d.l,{xs:"12",md:"12"},u.a.createElement(d.z,null,"Please enter name for new wishlist"),u.a.createElement(d.u,{type:"textField",rows:"9",id:"newWishListTextArea",placeholder:"Name..."})))),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"primary",onClick:this.addWishList},"Submit")," ",u.a.createElement(d.d,{color:"secondary",onClick:this.toggle},"Cancel"))),u.a.createElement(d.C,{isOpen:this.state.success,toggle:this.toggleSuccess,className:"modal-success "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleSuccess},"Add Wishlist Success"),u.a.createElement(d.D,null,"A new wishlist has been created!"),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"success",onClick:this.toggleSuccess},"OK")," ")),u.a.createElement(d.C,{isOpen:this.state.successDeleteRestaurant,toggle:this.toggleDeleteRestaurantSuccess,className:"modal-success "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleDeleteRestaurantSuccess},"Delete Restaurant Success"),u.a.createElement(d.D,null,"Restaurant has been deleted from your wishlist!"),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"success",onClick:this.toggleDeleteRestaurantSuccess},"OK")," ")),u.a.createElement(d.C,{isOpen:this.state.successDeleteWishList,toggle:this.toggleSuccessDeleteWishList,className:"modal-success "+this.props.className},u.a.createElement(d.F,{toggle:this.toggleSuccessDeleteWishList},"Delete Wishlist Success"),u.a.createElement(d.D,null,"Wishlist has been deleted!"),u.a.createElement(d.E,null,u.a.createElement(d.d,{color:"success",onClick:this.toggleSuccessDeleteWishList},"OK")," ")))}}]),t}(r.Component);t.default=m}}]);
//# sourceMappingURL=6.9f5d9b86.chunk.js.map