<template>
    <Navbar :user="user" />
    <div>
      <router-view :user="user" :login="login" :getCsrf="getCsrf"/>
    </div>
    <Footer />
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'
axios.defaults.withCredentials = true
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
export default {
  components: {
    Navbar,
    Footer
  },
  data () {
    return {
      user: {}
    }
  },
  computed: {
  },
  methods: {
    getCsrf () {
      axios.get('/api/getcsrf')
        .then(response => {
          console.log('Csrftoken recived')
        })
    },
    login (email, password) {
      axios({
        method: 'post',
        url: '/api/login',
        data: { email: email, password: password },
        headers: { 'X-CSRFToken': this.$cookies.get('csrftoken') }
      })
        .then(response => {
          this.user = response
          console.log(response)
        })
    },
    logout () {
      // Logout user in in backend and clear user data.
    },
    signup () {
      // Signup user in backend.
    },
    isAuthenticated () {
      // If user is not authenticated. Clear user data.
      axios({
        method: 'get',
        url: '/api/checkauth'//,
        // headers: { 'X-CSRFToken': this.$cookies.get('csrftoken') }
      }).then(response => {
        if (response.data.status === 'error') {
          console.log('error...')
          console.log(response.data.description) // something went wrong when ..
        } else if (response.data.status === 'isAuthenticated') {
          console.log('user is logged in')
          console.log(response.data)
          this.user.first_name = response.data.first_name
          this.user.email = response.data.email
        } else if (response.data.status === 'isNotAuthenticated') {
          console.log('User not authenticated. user data cleared')
          this.user = {}
        }
      })
        .catch(response => {
          console.log('error catch!')
          console.log(response)
        })
    }
  },
  created () {
    if (Object.keys(this.user).length) {
      this.isAuthenticated()
    }
  }
}
</script>

<style >
/**  Empty CSS file for your own CSS**/
html, body {
padding: 0px;
margin: 0px;
height: 100%;
}

#app {
min-height: 100%;
position: relative;
}

#navbar {
  background-color:#212529;
}
.footer{
    position: absolute;
    background-color: #344658;
    bottom: 0px;
    left: 0px;
    right: 0px;
    margin-top: 50px;
    padding-bottom: 10px;
    padding-left: 10px;
}

</style>
