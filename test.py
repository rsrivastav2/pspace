import { useState } from "react";

const DropdownComponent = () => {
  const [category, setCategory] = useState("");
  const [subCategories, setSubCategories] = useState([]);

  const options = {
    fruits: ["Apple", "Banana", "Orange"],
    vegetables: ["Carrot", "Broccoli", "Spinach"],
  };

  const handleCategoryChange = (event) => {
    const selectedCategory = event.target.value;
    setCategory(selectedCategory);
    setSubCategories(options[selectedCategory] || []);
  };

  return (
    <div>
      <label>Choose a Category:</label>
      <select value={category} onChange={handleCategoryChange}>
        <option value="">Select Category</option>
        <option value="fruits">Fruits</option>
        <option value="vegetables">Vegetables</option>
      </select>

      <label>Choose a Subcategory:</label>
      <select disabled={!category}>
        <option value="">Select Subcategory</option>
        {subCategories.map((item) => (
          <option key={item} value={item.toLowerCase()}>
            {item}
          </option>
        ))}
      </select>
    </div>
  );
};

export default DropdownComponent;
