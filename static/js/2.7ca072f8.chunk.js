(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{218:function(e,t,a){"use strict";var n=a(47),r=a(6),o=a(7),s=a(9),c=a(8),i=a(10),l=a(11),m=a(1),d=a.n(m),u=a(3),h=a(2),p=a.n(h),f=a(214),g=function(e){function t(e){var a;return Object(r.a)(this,t),(a=Object(s.a)(this,Object(c.a)(t).call(this,e))).handleClick=a.handleClick.bind(Object(l.a)(Object(l.a)(a))),a}return Object(i.a)(t,e),Object(o.a)(t,[{key:"handleClick",value:function(e){e.preventDefault()}},{key:"render",value:function(){var e=this,t=this.props,a=t.className,r=t.cssModule,o=t.header,s=t.mainText,c=t.icon,i=t.color,l=t.footer,m=t.link,h=(t.children,t.variant),g=Object(n.a)(t,["className","cssModule","header","mainText","icon","color","footer","link","children","variant"]),b="0"===h?{card:"p-3",icon:"p-3",lead:"mt-2"}:"1"===h?{card:"p-0",icon:"p-4",lead:"pt-3"}:{card:"p-0",icon:"p-4 px-5",lead:"pt-3"},E={style:"clearfix",color:i,icon:c,classes:""};E.classes=Object(f.mapToCssModules)(p()(a,E.style,b.card),r);var v={style:"h5 mb-0",color:i,classes:""};v.classes=p()(v.style,"text-"+E.color,b.lead);return d.a.createElement(u.e,null,d.a.createElement(u.f,Object.assign({className:E.classes},g),function(e){var t=p()(e,"bg-"+E.color,b.icon,"font-2xl mr-3 float-left");return d.a.createElement("i",{className:t})}(E.icon),d.a.createElement("div",{className:v.classes},o),d.a.createElement("div",{className:"text-muted text-uppercase font-weight-bold font-xs"},s)),function(){if(l)return d.a.createElement(u.g,{className:"px-3 py-2"},d.a.createElement("a",{className:"font-weight-bold font-xs btn-block text-muted",href:m,onClick:e.handleClick},"View More",d.a.createElement("i",{className:"fa fa-angle-right float-right font-lg"})))}())}}]),t}(m.Component);g.defaultProps={header:"$1,999.50",mainText:"Income",icon:"fa fa-cogs",color:"primary",variant:"0",link:"#"},t.a=g},279:function(e,t,a){e.exports=a.p+"static/media/logo.b32c1c44.png"},281:function(e,t,a){"use strict";a.r(t);var n=a(6),r=a(7),o=a(9),s=a(8),c=a(10),i=a(11),l=a(1),m=a.n(l),d=a(3),u=(a(237),a(277),a(279)),h=a.n(u),p=a(46),f=a.n(p),g=(a(212),a(213),a(218));var b=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(o.a)(this,Object(s.a)(t).call(this,e))).viewMore=function(e){a.props.history.push({pathname:"./restaurant",state:{restaurantID:e}}),sessionStorage.setItem("restaurantID",e)},a.viewMoreRecommend=function(e){a.props.history.push({pathname:"./restaurant",state:{restaurantID:a.state.recommendRestaurants[e].rid}}),sessionStorage.setItem("restaurantID",a.state.recommendRestaurants[e].rid)},a.viewMoreRecommend_eco=function(e){a.props.history.push({pathname:"./restaurant",state:{restaurantID:a.state.recommendEconomicRestaurants[e].rid}}),sessionStorage.setItem("restaurantID",a.state.recommendEconomicRestaurants[e].rid)},a.search=function(e){var t=a.state.original_restaurants.filter(function(e){return-1!==e.name.toLowerCase().indexOf(a.state.search.toLowerCase())||-1!==e.cname.toLowerCase().indexOf(a.state.search.toLowerCase())});a.setState({restaurants:t}),window.scrollTo({top:200,behavior:"smooth"})},a.input=function(e){a.setState({search:e.target.value})},a.state={data:[{name:"S",surname:"E",birthYear:1988,birthCity:"Karaman"},{name:"SH",surname:"E",birthYear:1988,birthCity:"Karaman"}],search:"",userID:sessionStorage.getItem("user_id"),original_restaurants:[],restaurants:[{rid:1,cid:1,cname:"pizza",name:"Metro Pizza",contact:"(702) 486-4368",location:"5757 Wayne Newton Blvd",star:2.5,photo_url:"https://s3-media1.fl.yelpcdn.com/bphoto/aAoUthFqsND23zdy1sZftw/o.jpg",longitude:-115.1391027,latitude:36.0808997},{rid:2,cid:6,cname:"Caffe",name:"Buddy V's Ristorante E Caffe",contact:"(702) 424-5786",location:"3930 Las Vegas Blvd S",star:3.5,photo_url:"https://s3-media4.fl.yelpcdn.com/bphoto/tpzXs9AmhxeZj7CcI2ZFRA/o.jpg",longitude:-115.138026,latitude:36.089494}],recommendRestaurants:[{rid:1,cid:1,cname:"pizza",name:"Metro Pizza",contact:"(702) 486-4368",location:"5757 Wayne Newton Blvd",star:2.5,photo_url:"https://s3-media1.fl.yelpcdn.com/bphoto/aAoUthFqsND23zdy1sZftw/o.jpg",longitude:-115.1391027,latitude:36.0808997},{rid:2,cid:6,cname:"Caffe",name:"Buddy V's Ristorante E Caffe",contact:"(702) 424-5786",location:"3930 Las Vegas Blvd S",star:3.5,photo_url:"https://s3-media4.fl.yelpcdn.com/bphoto/tpzXs9AmhxeZj7CcI2ZFRA/o.jpg",longitude:-115.138026,latitude:36.089494}],recommendEconomicRestaurants:[]},a.viewMore=a.viewMore.bind(Object(i.a)(Object(i.a)(a))),a.viewMoreRecommend=a.viewMoreRecommend.bind(Object(i.a)(Object(i.a)(a))),a.viewMoreRecommend_eco=a.viewMoreRecommend_eco.bind(Object(i.a)(Object(i.a)(a))),f.a.get("http://34.83.23.47:8080/api/restaurant").then(function(e){a.setState({restaurants:e.data,original_restaurants:e.data})},function(e){console.log(e)}),f.a.get("http://34.83.23.47:8080/api/recommendation/"+a.state.userID).then(function(e){a.setState({recommendRestaurants:e.data})},function(e){console.log(e)}),f.a.get("http://34.83.23.47:8080/api/cheap-recommendation").then(function(e){a.setState({recommendEconomicRestaurants:e.data})},function(e){console.log(e)}),a}return Object(c.a)(t,e),Object(r.a)(t,[{key:"render",value:function(){var e=this;return m.a.createElement("div",{style:{marginTop:"65vh"}},m.a.createElement("img",{src:h.a,className:"logo"}),m.a.createElement(d.v,{className:"search"},m.a.createElement(d.u,{onChange:this.input,placeholder:"search your favourite restaurants / category...",type:"text"}),m.a.createElement(d.x,{onClick:this.search,addonType:"append",style:{background:"orange",border:"none",color:"white"}},"Search")),m.a.createElement("div",{className:"banner"}),m.a.createElement("div",{className:"animated fadeIn"},m.a.createElement(d.J,null,m.a.createElement(d.l,{xs:"1",sm:"1",lg:"1"}),m.a.createElement(d.l,{xs:"7",sm:"7",lg:"7"},m.a.createElement("h2",{className:"text-dark"},m.a.createElement("i",{className:"fa fa-delicious"})," ",m.a.createElement("b",null,"Restaurants")),m.a.createElement(d.J,null,this.state.restaurants.map(function(t){return m.a.createElement(d.l,{lg:"6",key:t.rid},m.a.createElement(d.e,{className:"res",onClick:function(){return e.viewMore(t.rid)}},m.a.createElement("img",{className:"res-photo",src:t.photo_url}),m.a.createElement(d.f,null,m.a.createElement(d.k,null,m.a.createElement("b",{className:"res-title"},t.name)),m.a.createElement(d.j,{className:"res-subtitle"},t.location),m.a.createElement("span",{className:"res-tag ".concat(Math.random()<.5?"bg-primary":"bg-warning")},t.cname))))}))),m.a.createElement(d.l,{xs:"3",sm:"3",lg:"3"},m.a.createElement("h2",{className:"text-warning"},m.a.createElement("i",{className:"fa fa-star"})," ",m.a.createElement("b",null,"Recommendation")),this.state.recommendRestaurants.map(function(t,a){return m.a.createElement("div",{key:a,onClick:e.viewMoreRecommend.bind(e,a)},m.a.createElement(g.a,{header:t.name,mainText:t.cname+" for you",icon:"fa fa-star",color:"warning",footer:!0}))}),this.state.recommendEconomicRestaurants.map(function(t,a){return m.a.createElement("div",{key:a,onClick:e.viewMoreRecommend_eco.bind(e,a)},m.a.createElement(g.a,{header:t.name,mainText:"High Quality & Low Price",icon:"fa fa-fire",color:"danger",footer:!0}))})),m.a.createElement(d.l,{xs:"1",sm:"1",lg:"1"}))))}}]),t}(l.Component);t.default=b}}]);
//# sourceMappingURL=2.7ca072f8.chunk.js.map