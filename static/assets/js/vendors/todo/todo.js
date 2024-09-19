//*** Default Load Todo List
var todoLocal_store = localStorage.getItem("todosTbl");  
var todos;
var todoInputVal;	
var todoListData;
var listText;
if (todoLocal_store == null) {
	todos = ['Set Up Admin Configuration', 'How is this dmeki Admin ?'];
} else {
	todos = JSON.parse(todoLocal_store);
}
localStorage.setItem('todosTbl',JSON.stringify(todos));
	
//*** Check for data in localStorage
function checkTodos() {    		
	let html = "";	
	todos.forEach((todo,index) => {          
		html += `<li class="todo-itemlist">
					<div class="item-contain">
						<div class="todo-contian">
							<div class="todo-num">${index + 1}</div>
							<div class="todo-data">${todo}</div>
						</div>
						<div class="todo-action">
							<a href="javascript:void(0);" class="edit-todo text-success" data-val="${index}"><i class="fa fa-pencil"></i></a>
							<a href="javascript:void(0);" class="remove-todo text-danger ml_10" onclick='removeTodo(${index});'><i class="fa fa-trash"></i></a>
						</div>
					</div>
					<div class="list-error"></div>
				</li>`;		
			});
	$(".todo-list").empty().append(html);
	let html2 = `(${todos.length})` ;
	$(".card-header h4 .countTodo").empty().append(html2);
}

//*** Add items in todos
$(document).on('click', '.add-todo', function () { 	
	todoInputVal = $('input.todoInput').val();	
	let htmlAdd = "";
	if ($.trim(todoInputVal) !== ''){
		todos.push(todoInputVal);		
		localStorage.setItem('todosTbl',JSON.stringify(todos));	
	} 	
	todoListData = todos.forEach((todo,index) => { 
	// console.log(index)
	htmlAdd += `<li class="todo-itemlist">
			   <div class="item-contain">
				  <div class="todo-contian">
					<div class="todo-num">${index + 1}</div>
					<div class="todo-data">${todo}</div>
				  </div>
				  <div class="todo-action">
					<a href="javascript:void(0);" class="edit-todo text-success" data-val="${index}"><i class="fa fa-pencil"></i></a>
					<a href="javascript:void(0);" class="remove-todo text-danger ml_10" onclick='removeTodo(${index});'><i class="fa fa-trash"></i></a>
				  </div>
			   </div>
			   <div class="list-error"></div>
			</li>`;
		});
	$(".todo-list").empty().append(htmlAdd);     
	let htmlAdd_count = `(${todos.length})` ;
	$(".card-header h4 .countTodo").empty().append(htmlAdd_count);
	if ($.trim(todoInputVal) == '') {
		$(this).parents('.todo-content').find('.error').text('You must enter something!');
	} else {
		$(this).parents('.todo-content').find('.todo-list').append(todoListData);          
		$(this).parents('.todo-content').find('.error').empty();						
	}	
	$(this).siblings('input.todoInput').val('');                       
});
$('input.todoInput').keydown(function (event) {
	if (event.which == 13) {
		event.preventDefault();
		$('.add-todo').click();
	}
});

//*** Delete Todo List
let removeTodo = (index) => {
	todos.splice(index, 1);	
	localStorage.setItem("todosTbl", JSON.stringify(todos));
	checkTodos();
};

//*** Edit todo list
$(document).on('click', '.edit-todo', function () {
	$(this).removeClass('edit-todo');
    $(this).addClass('update-todo');
	$(this).html('<i class="fa fa-check text-primary" aria-hidden="true"></i>');
	listText = $(this).parents('.item-contain').find('.todo-data').html();	
	$(this).parents('.item-contain').find('.todo-data').attr('class', 'update-data');			
	$(this).parents('.item-contain').find('.update-data').html('<input type="text" class="todoEdit_input" value="' + listText + '" style="width: 100%;height: 40px;">');	
	$(this).parents('.item-contain').find('input').focus();
});

//*** Update todo list
$(document).on('click', '.update-todo', function () {
	var index;
	index = $(this).attr('data-val');
	var listText = $(this).parents('.item-contain').find('input').val();
	
	if ($.trim(listText) == '') {
		$(this).parents('.todo-itemlist').find('.list-error').text('You must enter something!');
	} else {		
        $(this).removeClass('update-todo');
        $(this).addClass('edit-todo');
		$(this).html('<i class="fa fa-pencil"></i>');
		$(this).parents('.item-contain').find('.update-data').attr('class', 'todo-data');
		$(this).parents('.item-contain').find('.todo-data').html(listText);
		$(this).parents('.todo-itemlist').find('.list-error').empty();
	}
	var index1 = todos.indexOf(todos[index]);
	console.log(index1)
	if (index1 !== -1) {
		todos[index1] = listText;
	}
	localStorage.setItem('todosTbl',JSON.stringify(todos));
});
$(document).keydown(function (event) {
	if (event.which == 13) {
		event.preventDefault();
		$('.update-todo').click();		
	}
});

//*** Line through the todo list
$(document).on('click', '.todo-data', function () {
	$(this).toggleClass('line-through');
});
checkTodos();