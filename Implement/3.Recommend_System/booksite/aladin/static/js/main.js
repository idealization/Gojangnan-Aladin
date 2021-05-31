class Controller {
    constructor(logdata) {this.logdata = logdata}
}

class KeyCtrl {
    constructor(key){
        this.key == key
        if (key == 'search') {
            this.data = Search.searching(key)
            return data
        }
    }
}

class Search {
    constructor (){}
    searching(key) {
        alert(key+'에 대한 book searching')
        return key+'에 대한 searching 결과'
    }
}

class DetailBook {
    constructor (){}
    getDetailBook(key) {
        alert(key+'에 대한 detail book')
        return key+'에 대한 detail book 결과'
    }
}

class Logger {
    constructor(data){
        alert('database에 로그 저장')
    }
}

