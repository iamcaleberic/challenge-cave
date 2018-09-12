class LinkedList {
  constructor() {
    this.nodes = []
  }

  getNode(value){
    return this.nodes.filter(node => node.value == value)
  }

  append(node){
    this.nodes.unshift(node)
  }

  as_json(){
    return JSON.stringify(this.nodes)
  }
}

class Node {
  constructor(value, next) {
    this.value = value
    this.next  = next
  }

   value(){
    return this.value
  }

   nextNode(){
    return this.next
  }
}
