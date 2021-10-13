<template>
    <label for="email">Email</label><br>
    <input type="email" name="email" id="email" v-model="email"><br>
    <label for="password">Password</label><br>
    <input type="password" name="password" id="password" v-model="password"><br>
    <button @click="login(email, password)">Login</button>
</template>
<script>
export default {
  props: ['user', 'login', 'test', 'getCsrf'],
  data () {
    return {
      email: '',
      password: ''
    }
  },
  created () {
    this.getCsrf()
    console.log('getCsrt()')
  }
}

</script>
