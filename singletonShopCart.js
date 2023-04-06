const Carrinho = (function(){
    let instance;

    function createInstance(){
        let produtos = [];

        function addProduto(produto){
            produtos.push(produto);
        }

        function getProduto(){
            return produtos;
        }

        function clearCarrinho(){
            produtos = [];
        }

        return{
            addProduto,
            getProduto,
            clearCarrinho

        };
    }

    return{
        getInstance: function(){
            if(!instance){
                instance = createInstance();
            }
            return instance;
        }
    }
})()

const carrinho = Carrinho.getInstance();

carrinho.addProduto({id: 001, nome: "Produto 1", preco: 10});
carrinho.addProduto({id: 002, nome: "Produto 2", preco: 20});
carrinho.addProduto({id: 003, nome: "Produto 3", preco: 30});
carrinho.addProduto({id: 004, nome: "Produto 4", preco: 40});
carrinho.addProduto({id: 005, nome: "Produto 5", preco: 50});
carrinho.addProduto({id: 006, nome: "Produto 6", preco: 60});
carrinho.addProduto({id: 007, nome: "Produto 7", preco: 70});

console.log(carrinho.getProduto());
carrinho.clearCarrinho();
console.log(carrinho.getProduto());