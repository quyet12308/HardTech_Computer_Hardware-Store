const manufacturers = [
    {
      imageUrl: "https://via.placeholder.com/100",
      name: "Hãng A",
      description: "Mô tả hãng A"
    },
    {
      imageUrl: "https://via.placeholder.com/100",
      name: "Hãng B",
      description: "Mô tả hãng B"
    }
  ];

  function renderTable() {
    const tbody = document.querySelector("#manufacturerTable tbody");
    tbody.innerHTML = "";
    manufacturers.forEach((manufacturer, index) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${index + 1}</td>
        <td><img src="${manufacturer.imageUrl}" alt="${manufacturer.name}" width="50"></td>
        <td>${manufacturer.name}</td>
        <td>${manufacturer.description}</td>
        <td>
          <button onclick="editManufacturer(${index})">Sửa</button>
          <button onclick="deleteManufacturer(${index})">Xóa</button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  }

  function addManufacturer(event) {
    event.preventDefault();
    const newImage = document.getElementById("newImage").files[0];
    const newName = document.getElementById("newName").value;
    const newDescription = document.getElementById("newDescription").value;

    const reader = new FileReader();
    reader.onload = function(e){
      const imageUrl = e.target.result;
      manufacturers.push({
        imageUrl: imageUrl,
        name: newName,
        description: newDescription
      });

      renderTable();

      document.getElementById("addManufacturerForm").reset();
    };
    reader.readAsDataURL(newImage);
  }

  function editManufacturer(index) {
    document.getElementById("editIndex").value = index;
    document.getElementById("editName").value = manufacturers[index].name;
    document.getElementById("editDescription").value = manufacturers[index].description;
    document.getElementById("editManufacturerForm").style.display = "block";
  }

  function updateManufacturer(event) {
    event.preventDefault();
    const index = document.getElementById("editIndex").value;
    const editImage = document.getElementById("editImage").files[0];
    const editName = document.getElementById("editName").value;
    const editDescription = document.getElementById("editDescription").value;

    if (editImage) {
      const reader = new FileReader();
      reader.onload = function(e) {
        manufacturers[index].imageUrl = e.target.result;
        manufacturers[index].name = editName;
        manufacturers[index].description = editDescription;

        renderTable();

        document.getElementById("editManufacturerForm").reset();
        document.getElementById("editManufacturerForm").style.display = "none";
      };
      reader.readAsDataURL(editImage);
    } else {
      manufacturers[index].name = editName;
      manufacturers[index].description = editDescription;

      renderTable();

      document.getElementById("editManufacturerForm").reset();
      document.getElementById("editManufacturerForm").style.display = "none";
    }
  }

  function deleteManufacturer(index) {
    if (confirm("Bạn có chắc chắn muốn xóa hãng sản xuất này không?")) {
      manufacturers.splice(index, 1);
      renderTable();
    }
  }

  document.getElementById("addManufacturerForm").addEventListener("submit", addManufacturer);
  document.getElementById("editManufacturerForm").addEventListener("submit", updateManufacturer);

  renderTable();