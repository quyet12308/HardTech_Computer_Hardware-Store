const categories = [
    { name: "Thể Loại A", description: "Mô tả thể loại A" },
    { name: "Thể Loại B", description: "Mô tả thể loại B" }
  ];
  
  function renderTable() {
    const tbody = document.querySelector("#categoryTable tbody");
    tbody.innerHTML = "";
    categories.forEach((category, index) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${index + 1}</td>
        <td>${category.name}</td>
        <td>${category.description}</td>
        <td>
          <button onclick="editCategory(${index})">Sửa</button>
          <button onclick="deleteCategory(${index})">Xóa</button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  }
  
  function addCategory(event) {
    event.preventDefault();
    const newCategoryName = document.getElementById("newCategoryName").value;
    const newCategoryDescription = document.getElementById("newCategoryDescription").value;
  
    categories.push({
      name: newCategoryName,
      description: newCategoryDescription
    });
  
    renderTable();
  
    document.getElementById("addCategoryForm").reset();
  }
  
  function editCategory(index) {
    document.getElementById("editIndex").value = index;
    document.getElementById("editCategoryName").value = categories[index].name;
    document.getElementById("editCategoryDescription").value = categories[index].description;
    document.getElementById("editCategoryForm").style.display = "block";
  }
  
  function updateCategory(event) {
    event.preventDefault();
    const index = document.getElementById("editIndex").value
    const editCategoryName = document.getElementById("editCategoryName").value;
    const editCategoryDescription = document.getElementById("editCategoryDescription").value;
  
    categories[index].name = editCategoryName;
    categories[index].description = editCategoryDescription;
  
    renderTable();
  
    document.getElementById("editCategoryForm").reset();
    document.getElementById("editCategoryForm").style.display = "none";
  }
  
  function deleteCategory(index) {
    if (confirm("Bạn có chắc chắn muốn xóa thể loại này không?")) {
      categories.splice(index, 1);
      renderTable();
    }
  }
  
  document.getElementById("addCategoryForm").addEventListener("submit", addCategory);
  document.getElementById("editCategoryForm").addEventListener("submit", updateCategory);
  
  renderTable();