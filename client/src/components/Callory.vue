<template>
  <div class="mt-2">
    <div class="font-weight-bold row">
      <div class="col-4">
        Daily Limit<br />
        <input
          class="mt-2 p-5 font-size-20"
          v-model="totalcall"
          readonly="isReadOnly"
        />
      </div>
      <div class="col-4">
        Current callories<br />
        <input
          class="mt-2 p-5 font-size-20"
          v-model="curentcall"
          readonly="isReadOnly"
        />
      </div>
      <div class="col-4">
        Total<br />
        <input
          class="mt-2 p-5 font-size-20"
          v-model="total"
          readonly="isReadOnly"
        />
      </div>
    </div>
    <div>
      <div class="row">
        <div class="col-4">
          <button class="btn font-weight-bold" @click="changeheight">
            Change Height
          </button>
          <button class="btn font-weight-bold" @click="changeweight">
            Change Weight
          </button>
        </div>
        <div class="col-4">
          <button class="btn font-weight-bold" @click="additem">
            Add Food
          </button>
        </div>
        <div class="col-4">
          <button class="btn font-weight-bold" @click="changeage">
            Change Age
          </button>
        </div>
      </div>
      <div class="row font-weight-bold py-2">
        <div class="col-4">Name</div>
        <div class="col-1 mx-4">Fat</div>
        <div class="col-1">Protien</div>
        <div class="col-1">Carbs</div>
        <div class="col-4 mx-3">Callories</div>
      </div>
    </div>
    <div class="font-weight-bold" v-if="foods.length == 0">No foods yet</div>
    <div
      v-else
      class="font-weight-bold py-2"
      v-for="(item, ItemIndex) in foods"
      :key="ItemIndex"
    >
      <div>
        <div>
          <div class="row">
            <div class="col-4">
              {{ item[0] }}
            </div>
            <div class="col-1 mx-4">
              {{ item[1] }}
            </div>
            <div class="col-1">
              {{ item[2] }}
            </div>
            <div class="col-1">
              {{ item[3] }}
            </div>
            <div class="col-4 mx-3">
              {{ item[4] }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      foods: [],
      totalcall: 0,
      curentcall: 0,
      total: 0,
      username: sessionStorage.getItem("username"),
      gender: "",
      weight: 0,
      height: 0,
      age: 0,
    };
  },
  async mounted() {
    await axios
      .post("http://localhost:5000/getdetials", { username: this.username })
      .then((Response) => {
        (this.gender = Response.data[0][0]),
          (this.weight = Response.data[0][1]),
          (this.height = Response.data[0][2]),
          (this.age = Response.data[0][3]);
      });
    if (this.gender == "male") {
      this.totalcall = 10 * this.weight + 6.25 * this.height - 5 * this.age + 5;
    } else if (this.gender == "female") {
      this.totalcall =
        10 * this.weight + 6.25 * this.height - 5 * this.age - 161;
    } else {
      this.totalcall = 0;
    }
    await axios
      .post("http://localhost:5000/getfood", { username: this.username })
      .then((Response) => {
        this.foods = Response.data;
      });
    for (let i = 0; i < this.foods.length; i++) {
      this.curentcall += parseInt(this.foods[i][4]);
    }
    this.total = parseInt(this.totalcall) - parseInt(this.curentcall);
  },
  methods: {
    additem() {
      this.$prompt("Enter Food Name").then((text1) => {
        this.$prompt("Enter Fat").then((text2) => {
          this.$prompt("Enter Protein").then((text3) => {
            this.$prompt("Enter carb").then((text4) => {
              let calls = text4 * 4 + text3 * 4 + text2 * 9;
              let food = {
                name: text1,
                fat: text2,
                prot: text3,
                carb: text4,
                callories: calls,
                username: this.username,
              };
              this.foods.push([text1, text2, text3, text4, calls]);
              this.curentcall += parseInt(calls);
              this.total = parseInt(this.totalcall) - parseInt(this.curentcall);
              axios.post("http://localhost:5000/addfood", food);
            });
          });
        });
      });
    },
    changeheight() {
      this.$prompt(
        "you current height is:\n" + this.height + "\n Change it?"
      ).then((text) => {
        axios
          .post("http://localhost:5000/changeheight", {
            height: text,
            username: this.username,
          })
          .then(() => {
            this.$alert("Done");
            window.location.reload();
          });
      });
    },
    changeweight() {
      this.$prompt(
        "you current height is:\n" + this.weight + "\n Change it?"
      ).then((text) => {
        axios
          .post("http://localhost:5000/changeweight", {
            weight: text,
            username: this.username,
          })
          .then(() => {
            this.$alert("Done");
            window.location.reload();
          });
      });
    },
    changeage() {
      this.$prompt(
        "you current height is:\n" + this.age + "\n Change it?"
      ).then((text) => {
        axios
          .post("http://localhost:5000/changeage", {
            age: text,
            username: this.username,
          })
          .then(() => {
            this.$alert("Done");
            window.location.reload();
          });
      });
    },
  },
};
</script>

<style>
.font-size-20 {
  font-size: 20px;
}
</style>